#!/usr/local/bin/python3
# _*_coding: utf-8

# Author: suntao
# Updated: Friday, July 22, 2016 at 1:50:16 PM


from __future__ import print_function
import subprocess
import os
import sys
from time import sleep


def install(name):
    if isinstance(name, str):
        subprocess.call(['sudo', 'pip3', 'install', name])
    elif isinstance(name, list):
        for i in name:
            if isinstance(i, str):
                subprocess.call(['sudo', 'pip3', 'install', i])
            else:
                raise SystemExit("非字符串参数，请安装包名称的合法性和正确性！")

    else:
        raise SystemExit('安装包的名称不是字符串，请检查下！')



REQUIREMENTS = ['tqdm', 'requests']
try:
    import requests as rq
    from tqdm import *
    import subprocess
except:
    print('Installing requirements: ' + str(REQUIREMENTS))
    subprocess.call(['sudo', 'pip3', 'install', '--upgrade', 'pip'])
    for req in REQUIREMENTS:
        install(req)

    # Then import again
    import requests as rq
    from tqdm import *


def run_env_build():
    pip_out = subprocess.check_output(['pip', 'list'])
    package_installed = pip_out.decode('utf-8')
    for pg in REQUIREMENTS:
        if pg not in package_installed.split('\n'):
            install(pg)
        else:
            pass


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
            data.write('{\n    version: %s \n}' % ver_no)
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
        print('Something goes wrong.')
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
    print('1. Start jetty server in about 30s...')
    cmd = 'sh suntao.sh'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    if stderr:
        print(stderr)
    if 'Started Jetty Server' in str(stdout):
        print('Jetty is ready for the next step.')
    else:
        print('Jetty is not ready yet, wait 10s more for ready...')
        sleep(10)


# Deploy the war file as docker container server in the cloud.
# Problem: sftp object can not find the file, but the file exists indeed.
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
    if stderr:
        print(stderr)
    print(stdout)

    return p.returncode


# Login on the remote beta server with zsh shell console available.
def go2zsh():
    cmd = "sshpass -p 'dfy!3fxxk%0JSI^s' ssh -t root@beta.menpuji.com 'cd /home/mpj/app ; zsh'"
    subprocess.call(cmd, shell=True)


def wait_time(time_arges):
    for i in tqdm(range(time_arges)):
        sleep(1)


# Main job function for all workflow.
def go_launch():
    pid = os.fork()
    if pid == 0:
        run_jetty()
        exit()
    print("1. Please wait 30s for jetty server's ready...")
    wait_time(30)
    sleep(2)
    print('√' * 66)
    print("Step1. is over! Let's clear the screen for the next step...")
    os.system('clear')
    print('2. Start generating appcache file...')

    os.chdir('menpuji-webapp') # building the appcache file for all of apps
    os.system('mvn antrun:run')
    print('\n')
    print('Appcache build finished!')
    os.system('clear')
    print('')
    if verify_appcache():
        print('3. Appcache文件生成有效! 验证程序执行完毕！')
    wait_time(5)
    sleep(2)
    print("Let's stop jetty server...")
    print('\n')
    os.system('mvn jetty:stop')
    os.system('clear')
    print('Jetty stopped!')
    wait_time(2)
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
    wait_time(2)
    print('War file build finished!')
    print('We are ready for launch. War file start transmit to remote server!')
    os.system('clear')
    print('We are ready for upload the war file.')
    dp = input('要上传到云端服务器启动部署吗？ \n > ')
    if dp.lower() == 'y':
        up_f = upload()
        print('The result of upload file is {}'.format(up_f))
    else:
        print('Nothing to do for this option. Bye!')
    print('自动打包流程已经结束，程序退出.')
    sys.exit()


# Main workflow
if __name__ == '__main__':
    print('Welcome to MPJ rocket launch program!')
    print('开始检查Python运行环境是否合格...')
    run_env_build()
    print('准备就绪，即将开始打包程序！')
    sleep(1)
    ask = input('Shall we get start? [Y]es or [N]o \n > ')
    while True:
        if ask.lower() == 'y' or ask.lower() == 'yes':
            ch_ver()
            break
        else:
            print('Okay, Bye!')
            sys.exit(0)
    go_launch()
