#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : test.py
@Software: PyCharm Community Edition
@Time    : 2018/9/19 21:26
"""

import numpy as np
import pandas as pd


data = np.random.randn(4, 4)
print(data)
print(data.shape, data.dtype)
data = data.reshape(2, 8)
print(data)
print(data.shape, data.dtype)
data = data.astype(np.int64)
print(data)
print(data.shape, data.dtype)

data_slice = data[:, 2:4]
print(data_slice)
data_slice[:, :] = 1
print(data_slice)
print(data)
