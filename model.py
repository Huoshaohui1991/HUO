#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mass = [50*i for i in range(1,12)]
length = [1.000,1.875,2.750,3.250,4.375,4.875,5.675,6.500,7.250,8.000,8.750]
F = np.polyfit(mass,length,1)
print(F)
P = np.poly1d(F)
print(P)
