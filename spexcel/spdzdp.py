#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/20 20:14
# @Author  : Geda
import requests
from bs4 import BeautifulSoup
import xlwt


start_url = 'https://www.dianping.com/search/category/41/10/g110'

def get_content(url):
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
        ]
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',

        #'Cookie':'_hc.v=c9e64cb5-ec29-a509-38ce-3f948f294335.1503308523; __utma=1.1371781487.1503308523.1503308523.1503308523.1; __utmb=1.5.10.1503308523; __utmc=1; __utmz=1.1503308523.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; _lxsdk_cuid=15e042bfcd636-00573ba9bf16bd-c313760-100200-15e042bfcd7c8; _lxsdk=15e042bfcd636-00573ba9bf16bd-c313760-100200-15e042bfcd7c8; s_ViewType=10; JSESSIONID=86BD760F85548C7B70D8A73A88B742A1; aburl=1; cy=41; cye=jinzhong; PHOENIX_ID=0a010918-15e042c3418-c7bd73b; __mta=156489988.1503308559858.1503308559858.1503308559858.1; _lxsdk_s=15e042bfcd9-14c-856-5e7%7C%7C22',
        'Cookie':'_hc.v=c9e64cb5-ec29-a509-38ce-3f948f294335.1503308523; __utma=1.1371781487.1503308523.1503308523.1503308523.1; __utmz=1.1503308523.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; _lxsdk_cuid=15e045af14dc8-0faaec4f20748c-c313760-100200-15e045af14ec8; _lxsdk=15e045af14dc8-0faaec4f20748c-c313760-100200-15e045af14ec8; s_ViewType=10; JSESSIONID=9C0E140936A02AAD2ED0B3777DCEBB74; aburl=1; cy=41; cye=jinzhong; PHOENIX_ID=0a010725-15e045b11ed-c8768e5; __mta=212646827.1503311630827.1503311630827.1503311630827.1; _lxsdk_s=15e045af150-c4-503-ce2%7C%7C22'
    }

    response = requests.get(url,headers=headers)
    return response.content


def region_url(html):
    #获取所有商区url
    soup = BeautifulSoup(html,'lxml')
    url_list = [i['href']for i in soup.find('div',id="bussi-nav").find_all('a')]
    return  url_list

def get_shop_url(html):

    soup = BeautifulSoup(html,'lxml')
    shop_list_url=soup.find_all('div' ,class_='tit')

    return [i.find('a')['href'] for i in shop_list_url]

def get_detal(html):

    soup = BeautifulSoup(html,'lxml')
    shop_name= soup.find('div',class_='breadcrumb').find('span').text
    price = soup.find('span',id='avgPriceTitle').text
    comment_score = soup.find('span',id='comment_score').find_all('span',class_='item')
    comments = soup.find('span',id = 'reviewCount').text
    adress = soup.find('span',itemprop='street-address').text
    print u'店名'+shop_name
    for cs in comment_score:
       print cs.text
    print u'评论数量'+comments
    print u'地址'+adress.strip()
    print u'人均价格'+price
    return(shop_name,comment_score[0].text,comment_score[1].text,comment_score[2].text,adress,price,comments)


if __name__ == '__main__':
    items = []
    base_url = 'https://www.dianping.com'
    html = get_content(start_url)
    region_url_list = region_url(html)
    region_url_list = [base_url+url for url in region_url_list]

    for region_url in region_url_list:
        try:
            for i in range(0,1):
                region_url=region_url + 'p' + str(i)


                shop_url_list =[base_url+url for url in get_shop_url(get_content(region_url)) ]

                for shop_url in shop_url_list:

                    detail_html = get_content(shop_url)
                    item = get_detal(detail_html)
                    items.append(item)
        except:
            continue
    new_table = 'DZDP.xls'
    wb =xlwt.Workbook(encoding='utf-8')
    ws =wb.add_sheet('test1')
    headDate = ['商户名字','口味屏风','环境评分','服务屏风','人均价格','地址','评论',]
    for colnum in range(0,7):
        ws.write(0,colnum,headDate[colnum],xlwt.easyxf('font: bold on'))
    index = 1
    lens=(len(items))
    for j in range(0,lens):
        for i in range(0,7):
            ws.write(index,i,items[j][i])
        index +=1
    wb.save(new_table)