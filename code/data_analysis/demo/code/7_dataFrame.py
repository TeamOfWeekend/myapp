#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : 7_dataFrame.py
@site    : 
@Time    : 2018/10/11 10:10
@Software: PyCharm Community Edition
"""


import pandas as pd
import numpy as np

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007],
        'pop': [1.5, 1.7, 1.9, 3.6, 2.4, 2.0, 2.9, 3.2]}
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'], index=np.arange(1, 17, 2))

print(frame)
print(frame.head(n=5))
print(frame['pop'])
print(frame.loc[3])
frame['debt'] = 0
print(frame)
print(frame.columns)
print(frame.index)
print(frame.values)

# frame = frame.reindex(np.arange(1, 20))
frame = frame.reindex(np.arange(1, 20), method='ffill')
# frame = frame.reindex(np.arange(1, 20), method='bfill')
print(frame)
