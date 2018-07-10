#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from pandas import DataFrame as df

column = load_iris().feature_names
data = load_iris().data
target = load_iris().target
df1 = df(data, columns=column)
df2 = df(target, columns=['target'])
data_df = pd.concat([df1, df2], axis=1)
print
data_df.shape
data_df.describe()
data_df[data_df['target']==0].describe()
data_df[data_df['target']==1].describe()
data_df[data_df['target']==2].describe()

data_df.cov()
data_df.corr()
from matplotlib import pyplot as plt
plt.plot(data_df[data_df['target']==0]['petal length (cm)'],data_df[data_df['target']==0]['petal width (cm)'],'r*',label='0')
plt.plot(data_df[data_df['target']==1]['petal length (cm)'],data_df[data_df['target']==1]['petal width (cm)'],'ro',label='1')
plt.plot(data_df[data_df['target']==2]['petal length (cm)'],data_df[data_df['target']==2]['petal width (cm)'],'bx',label='2')
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.legend(loc='best')
plt.grid()
plt.show()

from matplotlib import pyplot as plt

data0 = data_df[data_df['target'] == 0][
    ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].T
data1 = data_df[data_df['target'] == 1][
    ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].T
data1.columns = data0.columns
data2 = data_df[data_df['target'] == 2][
    ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].T
data2.columns = data0.columns
for i in range(0, 50):
    plt.plot([0, 1, 2, 3], data0[i], 'r-')
    plt.plot([0, 1, 2, 3], data1[i], 'b-')
    plt.plot([0, 1, 2, 3], data2[i], 'g-')

plt.xticks([0, 1, 2, 3], ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
plt.show()
from matplotlib import pyplot as plt
plt.hist(data_df[data_df['target']==0]['petal length (cm)'],color='blue',label='Class 0',alpha=0.5,bins=20)
plt.hist(data_df[data_df['target']==1]['petal length (cm)'],color='red',label='Class 1',alpha=0.5,bins=20)
plt.hist(data_df[data_df['target']==2]['petal length (cm)'],color='green',label='Class 2',alpha=0.5,bins=20)
plt.legend(loc='best')
plt.grid()
plt.show()
data_df.boxplot(by='target',layout=(2,2))
plt.show()