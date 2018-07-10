#!/usr/bin/python
# -*- coding: utf-8 -*-
#导入第三方包
from bs4 import BeautifulSoup
import time
import requests
# 设置伪头--用于防止反爬虫
headers = {'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
# 二手车主页的链接
url = 'http://shanghai.taoche.com/all/'
# 发送抓取链接的请求并进一步解析
res = requests.get(url, headers = headers).text
soup = BeautifulSoup(res,'html.parser')

# 抓取二手车品牌名称及对应的链接
car_brands = soup.findAll('div',{'class':'brand-name'})
# 根据HTML的标记搜索指定对象
car_brands = [j for i in car_brands for j in i] # 双重for循环的列表解析式
brands = [i.text for i in car_brands] # 去标签化处理

urls = ['http://shanghai.taoche.com' + i['href'] for i in car_brands] # 拼接完整的二手车品
# 构建空的列表，用于存放品牌的所有链接和品牌名称
target_urls = []
target_brands = []

# 通过for循环完成网页的解析，并生产链接
for b, u in zip(brands, urls):
    # 抓取各品牌二手车主页下的所有页码
    res = requests.get(u, headers=headers).text
    soup = BeautifulSoup(res, 'html.parser')

    # 查询出页数
    if len(soup.findAll('div', {'class': 'the-pages'})) == 0:
        pages = 1
    else:
        pages = int([page.text for page in soup.findAll('div', {'class': 'the-pages'})[0].findAll('a')][-2])

        # 为了防止反爬虫，这里每循环一次休眠3秒钟
    time.sleep(3)

    # 将链接存储起来
    for i in range(1, pages + 1):
        target_brands.append(b)
        target_urls.append(u + '?page=' + str(i) + '#pagetag')
        # 构建空列表，用于数据的存储
brand = []
title = []
boarding_time = []
km = []
discharge = []
sec_price = []
new_price = []

# 对每个链接发送请求
for b, u in zip(target_brands, target_urls):

    res = requests.get(u, headers=headers).text
    soup = BeautifulSoup(res, 'html.parser')

    # 统计每页二手车的数量
    N = len([i.findAll('a')[0]['title'] for i in soup.findAll('div', {'class': 'item_details'})])

    # 为防止报错，这里借用异常值处理办法
    try:
        # 二手车的品牌
        brands = (b + '-') * N
        brand.extend(brands.split('-')[:-1])

        # 二手车的名称
        title.extend([i.findAll('a')[0]['title'] for i in soup.findAll('div', {'class': 'item_details'})])

        # 二手车的上牌时间、行驶里程数等信息
        info = [i.findAll('li') for i in soup.findAll('ul', {'class': 'ul_news'})]
        boarding_time.extend([i[0].text[4:] for i in info])
        km.extend([i[1].text[4:] for i in info])

        # 二手车的排量标准
        discharge.extend([i[3].text[4:] for i in info])

        # 二手车的价格
        sec_price.extend([float(i.findAll('h2')[0].text[:-1]) for i in soup.findAll('div', {'class': 'item_price'})])

        # 新车的价格
        new_price.extend(
            [i.findAll('p')[0].text.split('\xa0')[0][5:].strip() for i in soup.findAll('div', {'class': 'item_price'})])

    except IndexError:
        print('索引错误')

        # 每3秒休眠一次
    time.sleep(3)
# 数据导出
import pandas as pd

# 先转化为数据框（记得转置）
cars_info = pd.DataFrame([brand,title,boarding_time,km,discharge,sec_price,new_price]).T

# 数据框变量的重命名
cars_info = cars_info.rename(columns={0:'Brand',
                                      1:'Name',
                                      2:'Boarding_time',
                                      3:'Km',
                                      4:'Discharge',
                                      5:'Sec_price',
                                      6:'New_price'})

# 数据的写出操作
cars_info.to_csv('second_cars_info.csv', index=False)