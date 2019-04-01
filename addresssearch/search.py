#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/17 15:46
# @Author  : Geda
import  xlrd
import  multiprocessing
import xlwt
def get_address_location():
    longitude = []
    latitude = []
    try:
        data = xlrd.open_workbook('addressofo.xls')
    except Exception, e:
        print str(e)
    table = data.sheet_by_name(u't_tasklaunch')
    nrows = table.nrows
    for rownum in range(1, nrows):
        row = table.row_values(rownum)

        latitude.append(row[1])
        longitude.append(row[2])
    return longitude, latitude, nrows

if __name__=='__main()__':
    num=[]
    num2=[]
    address_longitudes = (get_address_location()[0])
    address_latitudes = (get_address_location()[1])
    for  i  in  range(0,get_address_location()[2]-1):
        address_longitudes_m = address_longitudes[i] + 0.005
        address_longitudes_l = address_longitudes[i] - 0.005
        address_latitudes_m = address_latitudes[i] + 0.005
        address_latitudes_l = address_latitudes[i] - 0.005
        for j in range(0,get_address_location()[2]-1):
            num.append(address_longitudes[j])
        num2.append(len(num))
        num[:]=[]
    new_table = 'mission_and_mission_detail.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test1')
    index = 0
    k = 0
    lens = len(num2)
    while k < lens:
        for i in range(0, 1):
            ws.write(index, i, num2[k])
            k += 1
        index += 1
    wb.save(new_table)
