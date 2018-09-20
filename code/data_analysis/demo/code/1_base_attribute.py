#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : 1_base_attribute.py
@Software: PyCharm Community Edition
@Time    : 2018/9/20 22:41
"""


import numpy as np

data = np.array(np.arange(16), dtype=np.uint64)

print(data)
print(type(data))       # 类型 numpy.ndarray
print(data.ndim)        # 维度，轴，axes
print(data.shape)       # 形状
print(data.size)        # 大小，元素总个数
print(data.dtype)       # 数据类型
print(data.itemsize)    # 元素的字节个数
print(data.data)

# data = data.reshape(4, 4)     # reshape()无法修改本数组的形状
data.resize(2, 8)       # 修改形状
print(data)
data = data.T
print(data)
