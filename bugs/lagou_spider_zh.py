import requests
import json
import os
import sys
import pprint
from datetime import *
from xlsxwriter import *
from time import sleep
from random import randint
import ssl

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


# 自建传输配置器，制定SSL的版本``
class Ssl3HttpAdapter(HTTPAdapter):
    """"Transport adapter" that allows us to use SSLv3."""

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_SSLv3)

# 程序开始计时点
start_point = datetime.now()

#这里的header和上面的不同，大家试试看删掉一些还能不能获取数据
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "DNT": "1",
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": None,
    "X-Requested-With": "XMLHttpRequest" # 请求方式为XHR
}


# 计算该职位在拉勾网上查询出来的分页数函数
def get_pages(city, title, headers):
    ajax_url = 'https://www.lagou.com/jobs/positionAjax.json?city={0}'.format(city)
    post_param = {"first": "false", "pn": 1, "kd": title}
    r = requests.post(ajax_url, headers=headers, data=post_param, verify=True)
    total_items = 0
    if "content" in json.loads(r.text):
        total_items = json.loads(r.text)['content']['positionResult']['totalCount']
        # 计算分页数，分偶数和奇数两种情况
        if total_items % 15 == 0:
            pages = int(total_items / 15)
        else:
            pages = int(total_items // 15) + 1

    return total_items, pages


# 爬虫主要逻辑函数
def get_data(city, title, headers):
    # 循环程序起始时间点
    loop_start_point = datetime.now()
    # 设置多次循环来单独做数据请求，获取数据

    # 爬虫多有数据存储变量
    lagou_data = []

    pages = get_pages(city=city, title=title, headers=headers)[1]
    total_items = get_pages(city=city, title=title, headers=headers)[0]
    # print("1. 第一阶段开始 ---> 从网络获取数据...")
    print("在{0}与{1}相关的职位数据有{2}条。".format(city, title, total_items))
    print("此次爬虫程序总共要用{0}次循环来完成数据抓取...".format(pages))

    # 循环体内的url链接初始化
    ajax_url = 'https://www.lagou.com/jobs/positionAjax.json?city={0}'.format(city)

    # requests库中提供了session来维持较长数据的获取，看看能够避免SSL连接错误的问题
    with requests.Session() as s:
        s.mount('https://www.lagou.com', Ssl3HttpAdapter())
        for i in range(pages):
            # first 设置为False，我们用pn来翻页，pn：表示第几页，kd：表示搜索关键字
            post_param = {"first": "false", "pn": i, "kd": title}
            # 使用post方式，data里面存放我们的参数，可以通过浏览器调试工具获得
            r = s.post(url=ajax_url, data=post_param, headers=headers)
            if "content" in json.loads(r.text):
                rs_list = json.loads(r.text)["content"]["positionResult"]["result"]
                # print(rs_list["content"]["positionResult"]["result"][3])
                # print("This is {0} round loop running.".format(i))
                # print(len(rs_data))
                lagou_data = lagou_data + rs_list

            print(i * '+')
            sleep(randint(20, 25))

    if not len(lagou_data) is None:
        # for i in range(len(lagou_data)):
            # pp.pprint(lagou_data[i])
        print("This are {0} items in the list.".format(len(lagou_data)))
        return lagou_data
        # print("There are {0} items data is this list.".format(len(lagou_data[i])))
    else:
        try:
            sys.exit(0)
        except Exception as e:
            print("这个地方可能出错了(-: {0}".format(e))

    loop_end_point = datetime.now()
    print('爬虫工作完成，总耗时：{0}'.format(loop_end_point - loop_start_point))


# 写数据到Excel表中的函数
def writeExcel(ws, job, row=0, positionID='职位ID', positionName='职位名称', \
               salary='薪水', industryField='所在行业', financeStage='发展阶段', \
               workYear='工作经验', education='学历', firstType='职位大类', \
               city='所在城市', companySize='公司规模', companyFullName='公司全名', \
               fromCreateTime='发布天数', createTime='发布时间'):

    if row == 0:
        ws.write(row, 0, positionID)
        ws.write(row, 1, positionName)
        ws.write(row, 2, salary)
        ws.write(row, 3, industryField)
        ws.write(row, 4, financeStage)
        ws.write(row, 5, workYear)
        ws.write(row, 6, education)
        ws.write(row, 7, firstType)
        ws.write(row, 8, city)
        ws.write(row, 9, companySize)
        ws.write(row, 10, companyFullName)
        ws.write(row, 11, fromCreateTime)
        ws.write(row, 12, createTime)
    else:
        ws.write(row, 0, job['positionId'])
        ws.write_url(row, 1, 'https://www.lagou.com/jobs/%d.html' \
                     % job['positionId'], string=job['positionName'])
        ws.write(row, 2, job['salary'])
        ws.write(row, 3, job['industryField'])
        ws.write(row, 4, job['financeStage'])
        ws.write(row, 5, job['workYear'])
        ws.write(row, 6, job['education'])
        ws.write(row, 7, job['firstType'])
        ws.write(row, 8, job['city'])
        ws.write(row, 9, job['companySize'])
        ws.write(row, 10, job['companyFullName'])
        ws.write(row, 11, job['formatCreateTime'])
        ws.write(row, 12, job['createTime'])


# 写数据到Excel文件中
def save_Excel(data_file, file_name, sheet_name):
    # 创建第一个表格
    wb = Workbook(file_name)
    # 为表格文件创建一个工作表
    ws = wb.add_worksheet(sheet_name)
    print("开始写数据到Excel表格中...")
    for i in range(len(data_file)):
        writeExcel(ws, data_file[i], i)

    # 关闭文件流
    wb.close()
    print("写数据全部完成，您的数据已经妥善保存在电子表格文件中。")


# 打印一个可爱的箭头而已
def print_arrow():
    print('')
    # 箭头打印显示
    for i in range(3):
        print(2 * ' ' + '*')
    for i in range(3):
        print(i * ' ' + (5 - 2 * i) * '*' + i * ' ')
    print('')


if __name__ == "__main__":
    # 用户输入要查询的条件信息
    print("1. 初始化数据条件数据，需要用户输入...")
    city = input("哪个城市？" )
    title = input("什么职位？ ")
    excel_Name = '{0}-{1}相关职位数据原始表.xlsx'.format(city, title)
    sheet_Name = '{0}岗位原始数据'.format(title)
    print_arrow()
    sleep(2)

    print("2. 计算网络数据体量、计算分页数...")
    # 用第一页的数据请求来获取数据总量
    total_items, pages = get_pages(city, title, headers)
    print_arrow()
    sleep(2)


    print("3. 爬虫开始工作采集数据...")
    # 开始调用爬虫们工作采集数据
    lagou_data = get_data(city, title, headers)
    print_arrow()
    sleep(2)

    print("4. 将爬虫搜集到的数据写入Excel文件中...")
    # 将爬虫们搜集的数据写入到Excel表中
    save_Excel(lagou_data, excel_Name, sheet_Name)
    try:
        os.system('mv -f {0} ~/Desktop/求职之路/'.format(excel_Name))
    except:
        raise
    end_point = datetime.now()
    print_arrow()
    print("程序完成 -> 整个程序耗时{0}".format(end_point - start_point))
    print(40 * '√')
