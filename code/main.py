#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 21:54
"""


from vv_lib.vv_process.vprocess import VProcess

from myprocess.college.main import run_college
from myprocess.student.main import run_student

from myconfig.queues import queues

# 进程编号、名称、入口函数
process_def = ((1, 'college process', run_college),
               (2, 'student process', run_student))


if __name__ == "__main__":
    process_list = []

    for p in process_def:
        process_list.append(VProcess(p[0], p[1], p[2]))

    for p in process_list:
        p.start()

    for p in process_list:
        p.join()




