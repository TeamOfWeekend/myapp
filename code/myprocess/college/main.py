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

from myprocess.college.data_api import gColleges_info, gColleges
from myprocess.college.mythreads import thread_info, lock_info


def run_college(my_global):
    print("Process college start...")

    gLocks = []
    for lock in lock_info:
        gLocks.append(threading.Lock())

    my_global.paras['gLocks'] = gLocks
    my_global.paras['gColleges_info'] = gColleges_info
    my_global.paras['gColleges'] = gColleges

    threads = []
    for t in thread_info:
        threads.append(threading.Thread(target=t[2], args=(my_global, )))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Process college stop...")
