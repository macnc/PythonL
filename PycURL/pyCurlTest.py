#! /Users/suntao/anaconda2/bin/python
# _*_coding: utf-8

import StringIO
import pycurl
import os
import sys

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def test_gzip(input_url):
    t = Test()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL, input_url)
    c.perform()

    http_code = c.getinfo(pycurl.HTTP_CODE)
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)

    # print 'http_code http_size http_conn_time http_tran http_start_tran http_tran_total_time'
    print('_' * 68)
    print("%d  |  %d  |  %f  |  %f  |  %f  |  %f " % (http_code, http_size, http_conn_time, http_pre_tran, http_start_tran, http_total_time))
    print('_' * 68)


if __name__ == '__main__':
    input_url = sys.argv[1]
    test_time = int(sys.argv[2])

    if test_time is None:
        print("测试次数为空, 如果需要多次测试, 请输入测试次数.")
        test_gzip(input_url)
    else:
        for i in range(0, test_time):
            # print "第 %d 次测试开始" % i
            test_gzip(input_url)