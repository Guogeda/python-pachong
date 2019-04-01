#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/9 21:04
# @Author  : Geda
import  requests
import xlrd
import xlwt

def get_address():
    address=[]
    longitude=[]
    latitude=[]
    try:
        data = xlrd.open_workbook('addressdate.xlsx')
    except Exception,e:
        print str(e)
    table = data.sheet_by_name(u'Sheet1')
    nrows = table.nrows #hangshu
    for rownum in range(1,nrows):

        row = table.row_values(rownum)
        address.append(row[0])
        longitude.append(row[1])
        latitude.append(row[2])
    return address,longitude,latitude,nrows
def get_mobai_ofo(address,longitude,latitude):
    items=[]
    start_url = 'https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do'
    headers = {
        'referer': 'https://servicewechat.com/wx80f809371ae33eda/107/page-frame.html',
        'User-Agent': 'MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN',
        'Accept-Encoding': 'gzip',
    }
    data = {
        'longitude': longitude,
        'latitude': latitude,
        'citycode': '0354',
        'wxcode': '013CXPnj1n5dcy0AmZlj1QAHnj1CXPnq',
        'errMsg':'getLocation:ok'
    }
    requests.packages.urllib3.disable_warnings()
    req = requests.post(url=start_url,headers=headers,data=data,verify=False)
    print u'%s的膜拜单车数量：%s'%(address,len(req.json()['object']))

    for i  in  req.json()['object']:
        items.append(address)
        items.append(len(req.json()['object']))
        items.append(i.values()[3])
        items.append(i.values()[8])
        items.append(i.values()[7])
    return items
def get_tetail_sheet(address,items):
    print len(items)/5
    new_table = '%sdetail.xls'%address
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test1')
    headDate = ['地区', '数量', '编号', '经度', '纬度', ]
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
if __name__ =='__main__':
    address = (get_address()[0])
    longitudes=(get_address()[1])
    latitudes=(get_address()[2])
    all_detail=[]
    for i in range(0,get_address()[3]-1):
        #get_tetail_sheet(address[i],get_mobai_ofo(address[i],longitudes[i],latitudes[i]))
        all_detail.extend(get_mobai_ofo(address[i],longitudes[i],latitudes[i]))
    get_tetail_sheet('all',all_detail)
