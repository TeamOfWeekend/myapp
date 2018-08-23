#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main_college.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 21:38
"""

import time
import threading

from myprocess.college.mythreads import threads

def run_college():
    print("Process college start...")

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Process college stop...")
