#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : 6_series.py
@site    : 
@Time    : 2018/10/11 9:46
@Software: PyCharm Community Edition
"""

import numpy as np
import pandas as pd

a = pd.Series(np.arange(10), index=np.arange(1, 11))
a.name = 'mytest'
a.index.name = 'index'
print(a)
print(a[5])
print(a > 5)