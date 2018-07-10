#!/usr/bin/python
#-*-coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
# plt.style.use('ggplot')
path = '‪C:/Users/huoshaohui/Desktop/results.csv'
df = pd.read_csv('results.csv')
print(df)
# df_FIFA_all = df[df['tournament'].str.contains('FIFA', regex=True)]
# df_FIFA = df_FIFA_all[df_FIFA_all['tournament']=='FIFA World Cup']
# df_FIFA.loc[:,'date']
# pd.to_datetime(df_FIFA.loc[:,'date'])
# df_FIFA['year'] = df_FIFA['date'].dt.year
# df_FIFA['diff_score'] = df_FIFA['home_score']-df_FIFA['away_score']
# df_FIFA['win_team'] = ''
# df_FIFA['diff_score'] = pd.to_numeric(df_FIFA['diff_score'])
# print(df_FIFA)