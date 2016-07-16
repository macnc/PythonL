#!/usr/local/bin/python3
# _*_coding: utf-8

# Author: suntao
# Updated: Saturday, July 2, 2016 at 2:26:48 PM

import os
import sys
import subprocess
from time import sleep
import requests as rq
import pysftp as sftp


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


# Deploy the war file as docker container server in the cloud.
## Problem: sftp object can not find the file, but the file exists indeed.
def build_docker():
    import paramiko

    # Connect to remote host
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('beta.menpuji.com', username='root', password='dfy!3fxxk%0JSI^s')

    # Setup sftp connection and transmit this script
    sftp = client.open_sftp()
    if os.path.exists('dpl.py'):
        sftp.put(__file__, 'dpl.py')
        sftp.close()
    else:
        print('Plz copy the dpl file first!')
        sys.exit(1)

    # Run the trasmit script remotely without args and show its output.
    # SSHClient.exec_command() returns the tuple (stdin, stdout, stderr)
    stdout = client.exec_command('python /home/mpj/app/dpl.py')[1]
    for line in stdout:
        # Process each line in the remote output
        print(line)

    client.close()
    sys.exit(0)


# Upload the war package file to beta server
def upload():
    cmd = "sshpass -p 'dfy!3fxxk%0JSI^s' scp menpuji-webapp/target/menpuji.war root@beta.menpuji.com:/home/mpj/app"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stderr, stdout = p.communicate()
    out = stdout.decode('utf-8')
    err = stderr.decode('utf-8')

    return p.returncode

    '''
    # Another solution for upload file to remote server
    # 另外一种实现从本地上传文件到远程服务器的方式
    try:
        s = sftp.Connection(host='beta.menpuji.com', username='root', password='dfy!3fxxk%0JSI^s')

        remotepath = '/home/mpj/app/menpuji.war'
        localpath = 'menpuji-webapp/target/menpuji.war'
        s.put(localpath, remotepath)

        s.close()

    except Exception as e:
        print(str(e))
    '''

# Login on the remote beta server with zsh shell console available.
def go2zsh():
    cmd = "sshpass -p 'dfy!3fxxk%0JSI^s' ssh -t root@beta.menpuji.com 'cd /home/mpj/app ; zsh'"
    subprocess.call(cmd, shell=True)


# Main job function for all workflow.
def go_launch():
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
    os.system('clear')

    print("4. Let's delete the old target folder...")
    print('\n')
    FNULL = open(os.devnull, 'w')
    prm = subprocess.call(['rm', '-rf', 'target'], stdout=FNULL, stderr=subprocess.STDOUT)
    if prm == 0:
        print('Retcode is: %d. Then delete process works OK!' % prm)
        print('Old target folder has been removed!')
        sleep(2)
    else:
        print('Something goes wrong.')

    os.system('clear')
    print('5. Start packaging the project sourcecode...')
    print('\n')
    print('Change the work home folder...')
    os.chdir('..')


    print('Start packaging all of the project files...')
    os.system('mvn install')
    sleep(2)
    print('War file build finished!')
    print('\n')
    print('We are ready for launch. War file start transmit to remote server!')
    os.system('clear')
    print('We are ready for upload the war file.')
    upload()

    # os.system("sshpass -p 'dfy!3fxxk%0JSI^s' ssh root@beta.menpuji.com:/home/mpj/app")

# Main workflow
if __name__ == '__main__':
    print('Welcome to MPJ rocket launch program!')
    ask = input('Shall we get start? [Y]es or [N]o \n > ')
    while True:
        if ask.lower() == 'y' or ask.lower() == 'yes':
            ch_ver()
            break
        else:
            print('Okay, Bye!')
            sys.exit(0)
    go_launch()
