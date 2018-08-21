#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : process.py
@Software: PyCharm Community Edition
@Time    : 2018/8/21 21:59
"""

from vv_lib.vv_process.vprocess import VProcess

from myprocess.college.main import run_college
from myprocess.student.main import run_student
from prj_config.prj_queue import PrjQueue

# 进程编号、名称、入口函数
process_def = ((1, 'college process', run_college),
               (2, 'student process', run_student))

class PrjProcess:
    """添加类说明"""

    # Constructor
    def __init__(self):
        """Set the initial state of self, which includes the contents of
        sourceCollection, if it's present"""
        self.processes = []
        for p in process_def:
            self.processes.append(VProcess(p[0], p[1], p[2], PrjQueue()))


    def start(self):
        for p in self.processes:
            p.start()


    def join(self):
        for p in self.processes:
            p.join()
