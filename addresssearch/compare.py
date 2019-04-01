#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/15 11:36
# @Author  : Geda
import  xlrd
import  multiprocessing
import xlwt
def get_address_location():
    longitude = []
    latitude = []
    try:
        data = xlrd.open_workbook(u'附件三：新项目任务数据.xls')
    except Exception, e:
        print str(e)
    table = data.sheet_by_name(u't_tasklaunch')
    nrows = table.nrows
    for rownum in range(1, nrows):
        row = table.row_values(rownum)

        latitude.append(row[1])
        longitude.append(row[2])
    return longitude, latitude, nrows

def get_member_ofo():
    longitude = []
    latitude = []
    try:
        data = xlrd.open_workbook('membersofo.xlsx')
    except Exception, e:
        print str(e)
    table = data.sheet_by_name(u'Sheet1')
    nrows = table.nrows
    for rownum in range(1, nrows):
        row = table.row_values(rownum)

        latitude.append(row[1])
        longitude.append(row[2])
    return longitude, latitude, nrows

def  getdetail(j):


    try:
        data = xlrd.open_workbook('membersdetail.xlsx')
    except Exception, e:
        print str(e)
    table = data.sheet_by_name(u'Sheet1')

    row = table.row_values(j+1)
    xiane=(row[0])
    xinyu=(row[1])
    return xiane,xinyu

if __name__=='__main__':
    num =[]
    num2=[]
    lens=[]
    xianes=[]
    xinyus=[]
    address_longitudes_l=0
    address_longitudes_m=0
    address_latitudes_l=0
    address_latitudes_m=0
    pool = multiprocessing.Pool(processes=4)
    address_longitudes = (get_address_location()[0])
    address_latitudes = (get_address_location()[1])
    members_longitudes=(get_member_ofo()[0])
    members_latitudes=(get_member_ofo()[1])
    print len(address_longitudes),len(address_latitudes),len(members_latitudes),len(members_longitudes)
    for i in range(0, get_address_location()[2]-1):
        address_longitudes_m= address_longitudes[i]+0.005
        address_longitudes_l=address_longitudes[i]-0.005
        address_latitudes_m=  address_latitudes[i]+0.005
        address_latitudes_l=  address_latitudes[i]-0.005
        for j in range(0,get_member_ofo()[2]-1):
            if members_longitudes[j]<address_longitudes_m and members_longitudes[j]>address_longitudes_l:
                if members_latitudes[j]<address_latitudes_m and members_latitudes[j]>address_latitudes_l:
                    num.append(members_longitudes[j])
                    num.append(members_latitudes[j])
                    xianes.append(getdetail(j)[0])
                    xinyus.append(getdetail(j)[1])
        print len(num)

        lens.append(len(num))
        num2.append(len(num)/2)
        num2.append(sum(xianes))
        num2.append(sum(xinyus))
        num2.extend(num)
        num[:] = []
        xianes[:] = []
        xinyus[:] = []
    new_table = 'num_test_detail.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test1')
    index = 0
    k = 0
    lens = len(num2)
    while k < lens:
        for i in range(0, 3+lens[i]):
            ws.write(index, i, num2[k])
            k += 1
        index += 1
    wb.save(new_table)