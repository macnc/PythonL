#!/usr/local/bin/python3
# _*_coding: utf-8


import os
import subprocess
from time import sleep
import requests as rq


# Global variable for appcache of apps
mpos_appcache = 'src/main/webapp/pos/menpuji.appcache'
moffice_appcache = 'src/main/webapp/office/menpuji.appcache'
mclerk_appcache = 'src/main/webapp/clerk/menpuji.appcache'

# Global variable for version files
mpos_version = 'menpuji-webapp/src/main/webapp/pos/version.json'
moffice_version = 'menpuji-webapp/src/main/webapp/office/version.json'
mclerk_version = 'menpuji-webapp/src/main/webapp/clerk/version.json'

# File list for packaging
appcache_list = [mpos_appcache, moffice_appcache, mclerk_appcache]
appversion_list = [mpos_version, moffice_version, mclerk_version]


# Update the content of the file which we want to change.
def wr_file(file_list):
    ver_no = input('Plz enter the version number. > ')
    for file in file_list:
        with open(file, 'w') as data:
            data.write('{\n    version: %s \n}' % ver_no )
            print('File change completed!')


# Update the version files of mPOS, mOffice, mClerk.
def ch_ver():
    print('Hi, here are some option you can choose for your update: ')
    print('''
    1. mPOS
    2. mOffice
    3. mClerk
    4. mPOS and mOffice both
    5. mPOS and mClerk both
    6. mOffice and mClerk both
    7. All of them
    8. Just for testing, no need changing the version No.
    ''')
    options = {
        '1': [mpos_version],
        '2': [moffice_version],
        '3': [mclerk_version],
        '4': [mpos_version, moffice_version],
        '5': [mpos_version, mclerk_version],
        '6': [moffice_version, mclerk_version],
        '7': [mpos_version, moffice_version, mclerk_version],
        '8': []
    }
    while True:
        choose = input('Which option will be update? Please type the number: \n > ')
        if choose == '1':
            wr_file(options['1'])
            break
        elif choose == '2':
            wr_file(options['2'])
            break
        elif choose == '3':
            wr_file(options['3'])
            break
        elif choose == '4':
            wr_file(options['4'])
            break
        elif choose == '5':
            wr_file(options['5'])
            break
        elif choose == '6':
            wr_file(options['6'])
            break
        elif choose == '7':
            wr_file(options['7'])
            break
        elif choose == '8':
            pass
        else:
            print('Invalid input, plz choose the right number:')
            continue


# Test the status of jetty server for running.
def test():
    rtest = rq.get('http://localhost:9090/pos/index.html')
    if '处理中' in rtest.text:
        print('Jetty is available.')
        return True
    else:
        print('Someting goes wrong.')
        return False


# Verify the content of the appcache file.
def verify_appcache():
    '''
    This function is for check the appcahce file is valid or not.
    If the number of the content line is less than 20, then stop the whole
    process. Else it's valid appcache.
    '''
    for file in appcache_list:
        if os.path.exists(file):
            with open(file) as data:
                if len(data.readlines()) > 50:
                    return True
                else:
                    return False
        else:
            print('There are no such appcache files exist here!')


# Start the jettty server.
def run_jetty():
    print('1. Start jetty server in about 15s...')
    os.system('sh suntao.sh')


# Main function for all workflow.
def run():
    pid = os.fork()
    if pid == 0:
        run_jetty()
        exit()
    sleep(20)
    os.system('clear')
    print('2. Start generating appcache file...')
    print('\n' * 5)
    
    # building the appcache file for all of apps
    os.chdir('menpuji-webapp')
    os.system('mvn antrun:run')
    print('\n')
    print('Appcache build finished!')
    sleep(5)
    os.system('clear')
    if verify_appcache():
        print('3. Appcache文件生成有效! 验证程序执行完毕！')
        print('\n' * 3)
    else:
        exit()

    print("Let's stop jetty server...")
    print('\n')
    os.system('mvn jetty:stop')
    os.system('clear')
    print('Jetty stopped!')
    sleep(2)
    print('\n')
    print("4. Let's delete the old target folder...")
    print('\n')
    FNULL = open(os.devnull, 'w')
    retcode = subprocess.call(['rm', '-rf', 'target'], stdout=FNULL, stderr=subprocess.STDOUT)
    print('Retcode is: %d. Then delete process works OK!' % retcode)
    print('Old target folder has been removed!')
    print('\n' * 2)
    print('5. Start packaging the project sourcecode...')
    print('\n')
    os.chdir('..')
    os.system('mvn install')
    print('War file build finished!')
    print('\n')
    choice = input('6. 要上传war包到beta云端吗？ Y/N \n > ')
    if choice.lower() == 'y':
        os.system('sh launch.sh')
    elif choice == 'N':
        print('自动化打包程序执行完毕！')
    else:
        exit()
    
# Main workflow
#if __name__ == '__main__':
#    run() 
