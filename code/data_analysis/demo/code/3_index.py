#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : 3_index.py
@Software: PyCharm Community Edition
@Time    : 2018/9/20 23:00
"""

import numpy as np

data = np.array(np.arange(16))
data.resize(8, 2)
print(data)
print(data[[1, 0, 1, 0]])
print(data[[True, False, True, False, True, False, True, False]])
