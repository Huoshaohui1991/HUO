#!/usr/bin/python
# -*- coding: utf-8 -*-
# import pandas as pd
# f = open('C:/Users/huoshaohui/Desktop/uk_rain_2014.csv',encoding='utf-8')
# data = pd.read_csv(f)
# print(data.describe())
# headdata = data.head()
# print(headdata)
import goldsberry as gb
import pandas as pd
players = gb.PlayerList().players()
players = pd.DataFrame(players)
print(players.head())