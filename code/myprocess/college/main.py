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


def run_college(myprocess):
    print("Process colleged start...")
    queue = myprocess.queues.queues[0]
    queue.put(1)
    queue.put(2)
    queue.put(3)
    time.sleep(10)
    while not queue.empty():
        print(queue.get())
    print("Process colleged stop...")
