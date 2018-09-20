#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : 2_product.py
@Software: PyCharm Community Edition
@Time    : 2018/9/20 22:49
"""

import numpy as np

data1 = np.zeros((3, 4))
data2 = np.ones((3, 4))
data3 = np.empty((3, 4))
data4 = np.full((3, 4), fill_value=2)

data5 = np.zeros_like((3, 4))
data6 = np.eye(5)
data7 = np.identity(5)

print(data1)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)
print(data7)
