#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 21:41
# @Author  : Geda

import requests
import  re
import xlrd
import xlwt
import  multiprocessing
from  multiprocessing import  Pool

def get_addrss_ofo():
    address = []
    longitude = []
    latitude = []
    try:
        data = xlrd.open_workbook(u'附件三：新项目任务数据.xls')
    except Exception,e:
        print str(e)
    table = data.sheet_by_name(u't_tasklaunch')
    nrows = table.nrows
    for rownum in range(1,nrows):

        row = table.row_values(rownum)
        address.append(row[0])
        longitude.append(row[1])
        latitude.append(row[2])
    return   longitude,latitude,nrows

def get_address(longitude,latitude):
    key = 'bed295348775d996a2d6c658c4607ac9'
    start_url = 'http://restapi.amap.com/v3/geocode/regeo?output=xml&location=%s,%s&key=%s&radius=500&extensions=all' % (latitude,longitude,key)
    reg = requests.get(start_url).content

    num = r'<poi>(.*?)</poi>'
    num2 = re.findall(num,reg)


    address = r'<formatted_address>(.*?)</formatted_address>'
    address = re.findall(address, reg)

    type = '<type>(.*?)</type>'
    type = re.findall(type,reg)
    return  address,type[0],len(num2)


def get_detai(items):
    new_table = 'address_new_detail.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test1')
    headDate = ['地区','类型','附近建筑数量', '经度', '纬度' ]
    for colnum in range(0, 5):
        ws.write(0, colnum, headDate[colnum], xlwt.easyxf('font: bold on'))
    index = 1
    j = 0
    lens = (len(items))
    while j < lens:
        for i in range(0, 5):
            ws.write(index, i, items[j])
            j += 1
        index += 1
    wb.save(new_table)


if __name__ == '__main__':
    items=[]
    pool = multiprocessing.Pool (processes=4)
    longitudes = (get_addrss_ofo()[0])
    latitudes = (get_addrss_ofo()[1])
    #get_address(longitudes[2], latitudes[2])
    for i in range(0, get_addrss_ofo()[2]-1):
        pool.apply_async(items.extend(get_address(longitudes[i], latitudes[i])))

        items.append(longitudes[i])
        items.append(latitudes[i])
        print u'第%s个打印完成'%i
    get_detai(items)
    pool.close()
    pool.join()
