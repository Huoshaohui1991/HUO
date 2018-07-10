#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
data1 = {'a':0.,'b':1.,'c':2.}
s1 = pd.Series(data1)
s2 =pd.Series(data1,index=['b','c','d','a'])
print(s1)