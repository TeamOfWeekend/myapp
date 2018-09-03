#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : data_update.py
@Software: PyCharm Community Edition
@Time    : 2018/8/23 21:36
"""

import time
from myprocess.college.data_random import create_random_college_info, create_random_colleges


def thread_data_update(my_global):
    print('Thread college data update start..')

    gColleges_info = my_global.paras['gColleges_info']
    gColleges = my_global.paras['gColleges']

    create_random_college_info(gColleges_info)
    create_random_colleges(gColleges_info, gColleges)

    time.sleep(3)
    print('Thread college data update stop..')
