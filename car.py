#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from ggplot import *
import matplotlib.pyplot as plt
#导入油耗数据
vehicles = pd.read_csv("C:/Users/huoshaohui/Desktop/vehicles.csv")
print(vehicles)
print(len(vehicles))
#描述汽车油耗等数据
print(len(vehicles.columns))
print(vehicles.columns)
#查看年份信息
print(len(pd.unique(vehicles.year)))#总共的年份
print(min(vehicles.year))#最小年份
print(max(vehicles.year))#最大的年份
#查看变速箱类型
print(pd.value_counts(vehicles.trany))
#trany变量自动挡是以A开头，手动挡是以M开头；故创建一个新变量trany2：
vehicles["trany2"] = vehicles.trany.str[0]
print(pd.value_counts(vehicles.trany2))
#分析汽车油耗随时间变化的趋势
#- 先按照年份分组
grouped = vehicles.groupby('year')
#- 再计算其中三列的均值
averaged= grouped['comb08', 'highway08', 'city08'].agg([np.mean])
#- 为方便分析，对其进行重命名，然后创建一个‘year’的列，包含该数据框data frame的索引
averaged.columns = ['comb08_mean', 'highwayo8_mean', 'city08_mean']
averaged['year'] = averaged.index
print(averaged )
#- 使用ggplot包将结果绘成散点图
allCarPlt = ggplot(averaged, aes('year', 'comb08_mean')) + geom_point(colour='steelblue') + xlab("Year") + ylab("Average MPG") + ggtitle("All cars")
print(allCarPlt)
#- 去除混合动力汽车
criteria1 = vehicles.fuelType1.isin(['Regular Gasoline', 'Premium Gasoline', 'Midgrade Gasoline'])
criteria2 = vehicles.fuelType2.isnull()
criteria3 = vehicles.atvType != 'Hybrid'
vehicles_non_hybrid = vehicles[criteria1 & criteria2 & criteria3]
#print(vehicles_non_hybrid)
#- 将得到的数据框data frame按年份分组，并计算平均油耗
grouped = vehicles_non_hybrid.groupby(['year'])
averaged = grouped['comb08'].agg([np.mean])
averaged['hahhahah'] = averaged.index
print(averaged)
#- 查看是否大引擎的汽车越来越少
print(pd.unique(vehicles_non_hybrid.displ))
#- 去掉nan值，并用astype方法保证各个值都是float型的
criteria = vehicles_non_hybrid.displ.notnull()
vehicles_non_hybrid = vehicles_non_hybrid[criteria]
vehicles_non_hybrid.loc[:,'displ'] = vehicles_non_hybrid.displ.astype('float')
criteria = vehicles_non_hybrid.comb08.notnull()
vehicles_non_hybrid = vehicles_non_hybrid[criteria]
vehicles_non_hybrid.loc[:,'comb08'] = vehicles_non_hybrid.comb08.astype('float')
#- 最后用ggplot包来绘图
gasOnlineCarsPlt =  ggplot(vehicles_non_hybrid, aes('displ', 'comb08')) + geom_point(color='steelblue') +xlab('Engine Displacement') + ylab('Average MPG') + ggtitle('Gasoline cars')
print(gasOnlineCarsPlt)
#- 查看是否平均起来汽车越来越少了
grouped_by_year = vehicles_non_hybrid.groupby(['year'])
avg_grouped_by_year = grouped_by_year['displ', 'comb08'].agg([np.mean])
#- 计算displ和conm08的均值，并改造数据框data frame
avg_grouped_by_year['year'] = avg_grouped_by_year.index
melted_avg_grouped_by_year = pd.melt(avg_grouped_by_year, id_vars='year')
#- 创建分屏绘图
p = ggplot(aes(x='year', y='value', color = 'variable_0'), data=melted_avg_grouped_by_year)
p + geom_point() + facet_grid("variable_0",scales="free") #scales参数fixed表示固定坐标轴刻度，free表示反馈坐标轴刻度
print(p)
#- 首先查看cylinders变量有哪些可能的值
print(pd.unique(vehicles_non_hybrid.cylinders))
#- 再将cylinders变量转换为float类型，这样可以轻松方便地找到data frame的子集
vehicles_non_hybrid.cylinders = vehicles_non_hybrid.cylinders.astype('float')
pd.unique(vehicles_non_hybrid.cylinders)
#- 现在，我们可以查看各个时间段有四缸引擎汽车的品牌数量
vehicles_non_hybrid_4 = vehicles_non_hybrid[(vehicles_non_hybrid.cylinders==4.0)]

grouped_by_year_4_cylinder =vehicles_non_hybrid_4.groupby(['year']).make.nunique()
#fig = grouped_by_year_4_cylinder.plot()
plt.plot(grouped_by_year_4_cylinder)
plt.xlabel("Year")
plt.ylabel("Number of 4-Cylinder Maker")
plt.show()
# -  查看各年有四缸引擎汽车的品牌的列表，找出每年的品牌列表
grouped_by_year_4_cylinder = vehicles_non_hybrid_4.groupby(['year'])
unique_makes = []
from functools import reduce
for name, group in grouped_by_year_4_cylinder:
    # list中存入set(),set里包含每年中的不同品牌
    unique_makes.append(set(pd.unique(group['make'])))
unique_makes = reduce(set.intersection, unique_makes)
print(unique_makes)
#创建一个空列表，最终用来产生布尔值Booleans
boolean_mask = []
#用iterrows生成器generator遍历data frame中的各行来产生每行及索引
for index, row in vehicles_non_hybrid_4.iterrows():
    #判断每行的品牌是否在此前计算的unique_makes集合中,在将此布尔值Blooeans添加在Booleans_mask集合后面
    make = row['make']
    boolean_mask.append(make in unique_makes)
df_common_makes = vehicles_non_hybrid_4[boolean_mask]

#-  先将数据框data frame按year和make分组，然后计算各组的均值
df_common_makes_grouped = df_common_makes.groupby(['year', 'make']).agg(np.mean).reset_index()
#-  最后利用ggplot提供的分屏图来显示结果
oilWithTime = ggplot(aes(x='year', y='comb08'), data = df_common_makes_grouped) + geom_line() + facet_wrap('make')
print(oilWithTime)