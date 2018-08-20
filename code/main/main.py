#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 21:54
"""

from queue import Queue
from vv_lib.vv_process.vprocess import VProcess
from vv_lib.vv_queue.vqueue import VQueue

from colleged import run_college
from studentd import run_student


process_def = ((1, 'college process', run_college),
                (2, 'student process', run_student))

queue_def = ((1, 'send queue', 20),
              (2, 'recv queue', 20))

if __name__ == "__main__":
    queue_list = []
    for q in queue_def:
        queue_list.append(VQueue(q[0], q[1], q[2]))
    # run_college()
    process_list = []
    for p in process_def:
        process_list.append(VProcess(p[0], p[1], p[2], queue_list))

    for p in process_list:
        p.start()

    for p in process_list:
        p.join()

