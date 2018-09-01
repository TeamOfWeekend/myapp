#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main_college.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 21:38
"""
import threading

from vv_lib.vv_college.college import ImCollege
from vv_lib.vv_college.types import CollegeEnum

from myprocess.college.mythreads import thread_info, lock_info
from myprocess.college.data_api import gColleges


def run_college(my_global):
    print("Process college start...")

    gLocks = []
    for lock in lock_info:
        gLocks.append(threading.Lock())

    for collegeE in CollegeEnum:
        college = ImCollege()
        college.name = collegeE.name
        college.id = collegeE.value
        college.createRandomAttrs()
        print("%s %d" % (college.name, college.getStudentNum()))
        gColleges.append(college)

    my_global.paras['gLocks'] = gLocks
    my_global.paras['gColleges'] = gColleges

    threads = []
    for t in thread_info:
        threads.append(threading.Thread(target=t[2], args=(my_global, )))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Process college stop...")
