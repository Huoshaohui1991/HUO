#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns = ['a','b','c']
df = pd.DataFrame(data=data, index=index,columns=columns)
print(df.loc[:,'d'])
