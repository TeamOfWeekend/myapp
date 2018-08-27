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
from vv_lib.vv_college.college import ImCollege
from vv_lib.vv_college.types import CollegeEnum


gCollegeList = []


def thread_data_update(my_global, gLocks):
    print('Thread college data update start..')
    for collegeE in CollegeEnum:
        college = ImCollege()
        college.name = collegeE.name
        college.id = collegeE.value
        college.createRandomAttrs()
        print("%s %d" % (college.name, college.getStudentNum()))
        gCollegeList.append(college)

    time.sleep(3)
    print('Thread college data update stop..')
