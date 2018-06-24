# -*- coding: utf-8 -*-

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


# Create HTTPAdapter with specific SSL ssl_version
class Ssl3HttpAdapter(HTTPAdapter):
    """"Transport adapter" that allows us to use SSLv3."""

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_SSLv3)

# Start point for running the code.
start_point = datetime.now()

# Defination of the headers data, please try other option of the datasets
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "DNT": "1",
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": None,
    "X-Requested-With": "XMLHttpRequest" # request as XHR
}


# Compute the page number of lagou website for eachi request.
def get_pages(city, title, headers):
    ajax_url = 'https://www.lagou.com/jobs/positionAjax.json?city={0}'.format(city)
    post_param = {"first": "false", "pn": 1, "kd": title}
    r = requests.post(url=ajax_url, headers=headers, data=post_param, verify=True)
    total_items = 0
    if "content" in json.loads(r.text):
        total_items = json.loads(r.text)['content']['positionResult']['totalCount']
        # Two ways: ood number and even number for pages.
        if total_items % 15 == 0:
            pages = int(total_items / 15)
        else:
            pages = int(total_items // 15) + 1

    return total_items, pages


# main function of the data scrapy.
def get_data(city, title, headers):
    # loop start.
    loop_start_point = datetime.now()


    # The variable for storaging all of the datasets.
    lagou_data = []

    pages = get_pages(city, title, headers)[1]
    total_items = get_pages(city, title, headers)[0]
    # print("1. Phase 1 ---> Get the data from lagou XHR requests...")
    print("There are{0} position data records related with {1} in {2}".format(total_items, title, city))
    print("We need {0} times loop to finish this scrapy...".format(pages))

    # ajax url requests
    ajax_url = 'https://www.lagou.com/jobs/positionAjax.json?city={0}'.format(city)

    # Establish a session object for keep long time connections.
    with requests.Session() as s:
        s.mount('https://www.lagou.com', Ssl3HttpAdapter())
        for i in range(pages):
            # first set to False, pn: page, kd: keywords
            post_param = {"first": "false", "pn": i, "kd": title}
            r = s.post(url=ajax_url, data=post_param, headers=headers)
            if "content" in json.loads(r.text):
                rs_list = json.loads(r.text)["content"]["positionResult"]["result"]
                lagou_data = lagou_data + rs_list

            print(i * '+')
            sleep(randint(20, 25))

    if not len(lagou_data) is None:
        print("This are {0} items in the list.".format(len(lagou_data)))
        return lagou_data
    else:
        try:
            sys.exit(0)
        except Exception as e:
            print("Something goes wrong. (-: {0}".format(e))

    loop_end_point = datetime.now()
    print('Scrapy works done. Totally costs：{0}'.format(loop_end_point - loop_start_point))


# The function of writing data to excel file.
def writeExcel(ws, job, row=0, positionID='Position ID', \
               positionName='Position Name', salary='Salary', \
               industryField='Industry', financeStage='Finance Stage', \
               workYear='Work Year', education='Education', firstType='Job Type',
               city='City', companySize='Company Size', \
               companyFullName='Company Full Name', \
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
        ws.write(row, 1, job['positionName'])
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


# Save all of the data from lagou website
def save_Excel(data_file, file_name, sheet_name):
    # Create a Excel File.
    wb = Workbook(file_name)
    # Create a work sheet for excel file.
    ws = wb.add_worksheet(sheet_name)
    print("Start writing data to Excel file...")
    for i in range(len(data_file)):
        writeExcel(ws, data_file[i], i)

    # close the file streaming.
    wb.close()
    print("All of the data has been writen to the Excel file.")


# Print out a pretty arrow
def print_arrow():
    print('')
    # arrow print out
    for i in range(3):
        print(2 * ' ' + '*')
    for i in range(3):
        print(i * ' ' + (5 - 2 * i) * '*' + i * ' ')
    print('')


if __name__ == "__main__":
    # Input the information from terminal
    print("1. Initializae the conditional information...")
    city = input("City? " )
    title = input("Position? ")
    excel_Name = '{0}_{1}_position_data.xlsx'.format(city, title)
    sheet_Name = '{0}_Original_data'.format(title)
    print_arrow()
    sleep(2)

    print("2. Compute the data size and pages...")
    # Compute the data size with first requests.
    total_items, pages = get_pages(city, title, headers)
    print_arrow()
    sleep(2)


    print("3. Scrapy start come out to work...")
    # Get the data from scrapy.
    lagou_data = get_data(city, title, headers)
    print_arrow()
    sleep(2)

    print("4. Write the data form scrapy to Excel...")
    # Save all of the data to Excel.
    save_Excel(lagou_data, excel_Name, sheet_Name)
    try:
        os.system('mv -f {0} ~/datasets/'.format(excel_Name))
    except:
        raise
    end_point = datetime.now()
    print_arrow()
    print("All jobs' done! -> Totally cost {0} in this program.".format(end_point - start_point))
    print(40 * '√')
