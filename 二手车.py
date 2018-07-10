#!/usr/bin/python
# -*- coding: utf-8 -*-
# 导入第三方包

import bs4
import time

# 设置伪头--用于防止反爬虫

headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

# 二手车主页的链接
url = 'http://shanghai.taoche.com/all/'

# 发送抓取链接的请求并进一步解析
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, 'html.parser')

# 抓取二手车品牌名称及对应的链接
car_brands = soup.findAll('div', {'class': 'brand-name'})
# 根据HTML的标记搜索指定对象
car_brands = [j for i in car_brands for j in i]  # 双重for循环的列表解析式
brands = [i.text for i in car_brands]  # 去标签化处理

urls = ['http://shanghai.taoche.com' + i['href'] for i in car_brands]  # 拼接完整的二手车品牌链接