#!/usr/bin/python
# _*_coding: utf-8


import os
import sys
import exceptions
import itertools
from time import sleep
from os import path
import human_curl as hurl


'''
本脚本完成门铺集web-app的Tomcat docker容器服务部署, 下面代码脚本为临时的实现方案，后续可能
会根据发布服务的docker设计方案变化而发生变化。脚本完成的详细工作在run()方法的help doc中有详
细的说明。
'''

# 生成docker容器配置变量信息的函数
def docker():
    '''
    此函数将返回一个字典数据类型，存储了生成docker容器所需要的一切配置信息：
    1. 需要发版本的预发布版本号码
    2. 需要发布的红绿分支信息(包含有:旗子颜色和对应的端口号)
    3. 此次发布的根目录名字
    4. 此次发布生成的docker容器名字
    5. 此次发布的web-app源代码投放的具体目录位置
    '''
    docker_config = {}
    docker_config['version'] = int(raw_input('请输入你要发布的版本号，只写数字不必加字母v: '))
    while True:
        flag = raw_input('想发版本是吧？你想要发红(R)？还是发绿(G)？ ')
        if flag.lower() == 'r':
	        docker_config['flag'] = 'red'
	        docker_config['port'] = 9001
	        break
        elif flag.lower() == 'g':
	        docker_config['flag'] = 'green'
	        docker_config['port'] = 9000
	        break
        else:
	        print '请输入英文字母(R)或者(G)，其他值都不被接受!!!'
	        continue
    docker_config['root_path'] = 'mAPP-docker-v{version}'.format(**docker_config)
    docker_config['container'] = 'mpj-V{version}-{flag}'.format(**docker_config)
    docker_config['war_target'] = './{root_path}/{flag}/webapp/'.format(**docker_config)
    print '本次要发布Web服务的目标目录位置是: {war_target}'.format(**docker_config)
    print '本次要测试的主工程目录名为: mAPP-docker-v{version}'.format(**docker_config)
    print '本次发布要生成的容器名为: mpj-V{version}-{flag}'.format(**docker_config)

    return docker_config


# 创建版本发布时，蓝绿发布的的目录结构
def new_folder(docker_config):
    '''
    用法：
    1. 调用此函数时，需要用户手动在控制台输入要发布的版本号
    2. 根据输入的版本号目录，自动生成docker的蓝绿发布模板目录结构
    '''

    rg_folders = ['green', 'red']
    service_folders = ['webapp', 'log']

    for rg, service in itertools.product(rg_folders, service_folders):
        os.makedirs(os.path.join(docker_config['root_path'], rg, service))

    print 'docker测试工程目录创建成功！ 下面是目录结构: '
    os.system('tree {root_path}'.format(**docker_config))


# 解压对应的版本war包到对应的目录
def unzip_war(war_file, target):
    '''
    此函数将参数指定的war文件解压到第二个参数指定的目录位置
    1. war_file为war包文件名字。参数类型：字符串
    2. target参数为war包解压到的具体目录位置。参数类型：字符串
    '''
    print '本次解压过程会将%s文件将会被解压到%s' % (war_file, target)
    os.system('unzip %s -d %s' % (war_file, target))


# 创建Docker镜像创建对应的蓝绿发布容器, 启动容器服务
def new_container(docker_config):
    '''创建容器的方法需要考虑以下设计问题：
    1. 尽可能把所有公用的数据抽取出来存储在一个公共数据对象中，方便全局的随时存取使用
    2. 对于创建容器的命令中，关于本次发布的所有公共信息可以使用字典的unpacking语法来实现替换
    3. 第一个版本的容器创建方法，先简单调用shell命令实现，优雅的代码后续继续重构

    函数用法：
    传入的参数docker_config为一个字典数据类型，该数据对象中必须包含有生成docker容器指令对应
    的所有数据信息：
    1. version: 版本号，类型为数字，int和float都可以
    2. flag: 红绿发布的开关标示，只有两个值是有效的：green或者red
    3. port: 红绿发布分别对应的端口值，这个在docker配置信息生成函数中有定义:9000或者9001
    4. root_path: 本次发布生成版本目录的根目录名
    '''
    ac_code = None
    print '即将为此次发布创建容器...'
    if docker_config['flag'] == 'green':
        ac_code = 'docker run -d -p {port}:9000 -v /home/mpj/app/{root_path}/\
        {flag}/webapp/:/tomcat/webapps/menpuji -v /home/mpj/app/{root_path}/\
        {flag}/log:/tomcat/logs --name mpj-V{version}-{flag} \
        tomcat_menpuji:menpuji_webapp_beta_java_node'.format(**docker_config)

        try:
            os.system(ac_code)
        except:
            print 'shell命令有误，请核查.'
            sys.exit()
        print '此次发布为绿色分支，属于预备正式发布阶段，容器已经创建并启动完毕！'

    elif docker_config['flag'] == 'red':
        ac_code = 'docker run -d -p {port}:9000 -v /home/mpj/app/{root_path}/\
        {flag}/webapp/:/tomcat/webapps/menpuji -v /home/mpj/app/{root_path}/\
        {flag}/log:/tomcat/logs --name mpj-V{version}-{flag} \
        tomcat_menpuji:menpuji_webapp_beta_java_node'.format(**docker_config)

        try:
            os.system(ac_code)
        except:
            print 'shell命令有误，请核查.'
            sys.exit()
        print '此次发布为红色分支，为您做好测试的准备。即将为您测试容器服务是否正常...'


# 测试上线服务的可用性
def test(docker_config):
    t1 = hurl.get('http://beta.menpuji.com:{port}/pos/index.html'.format(**docker_config))
    s_code = t1._status_code
    if s_code == 200:
        print '测试服务器部署完毕，可以愉快的进行业务测试了。^_^**'
    else:
        print '服务器部署不成功，查一下代理服务器配置信息。<..>'
        sys.exit()


# 主控制程序代码
def run():
    '''
    主控制代码顺序执行以下任务：
    1. 先判断本次发布的app目录中是否存在有预设的war包文件，没的话直接退出发布程序
    2. 根据发布者输入的版本信息生成本次发布的基础信息数据
    3. 为本次发布创建docker发布目录（样板文件夹）
    4. 将指定文件名的war文件解压到对应的发布目录中
    5. 根据指定的发布目录，为本次发布创建docker容器实例，并启动docker服务
    6. docker容器启动后，随后启动测试程序，检测对应的tomcat服务器的状态是否正常
    7. 测试通过后，完成发布通知。退出主控制程序。
    '''
    if path.isfile('menpuji.war'):
        print 'war包已经就绪，请确认war包的正确性: 4s确认时间...'
        sleep(4)
        docker_config = docker()
        new_folder(docker_config)
        unzip_war('menpuji.war', docker_config['war_target'])
        new_container(docker_config)
        test_service(docker_config)
        sys.exit()
    else:
        print '请上传war包文件，然后重新启动此自动化部署脚本程序.'
        sys.exit()
