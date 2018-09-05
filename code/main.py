#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 21:54
"""

import platform
import os
import sys

from vv_lib.vv_process.vprocess import VProcess

from myprocess.college.main import run_college
from myprocess.student.main import run_student

from common.myglobal import MyGlobal

# 进程编号、名称、入口函数
process_def = ((1, 'college process', run_college),
               (2, 'student process', run_student))


# find current path  os what system we're on
if "Windows" == platform.system():
    sys.path.append(os.path.abspath('.') + "\\vv_lib\\vv_college")
    sys.path.append(os.path.abspath('.') + "\\vv_lib\\vv_ipc_msg")
    sys.path.append(os.path.abspath('.') + "\\vv_lib\\vv_person")
    sys.path.append(os.path.abspath('.') + "\\vv_lib\\vv_process")
    sys.path.append(os.path.abspath('.') + "\\vv_lib\\vv_queue")
else:
    sys.path.append(os.path.abspath('.') + "/libs")
    sys.path.append(os.path.abspath('.') + "/vv_lib/vv_college")
    sys.path.append(os.path.abspath('.') + "/vv_lib/vv_ipc_msg")
    sys.path.append(os.path.abspath('.') + "/vv_lib/vv_person")
    sys.path.append(os.path.abspath('.') + "/vv_lib/vv_process")
    sys.path.append(os.path.abspath('.') + "/vv_lib/vv_queue")

if __name__ == "__main__":
    process_list = []
    my_global = MyGlobal()

    for p in process_def:
        process_list.append(VProcess(p[0], p[1], p[2], my_global))

    for p in process_list:
        p.start()

    for p in process_list:
        p.join()




