#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : 4_plot.py
@site    : 
@Time    : 2018/9/22 16:59
@Software: PyCharm Community Edition
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
plt.plot(x, y, 'bp--')
plt.show()

# data = np.array(x)
# data.plot(kind='box')
