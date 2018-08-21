#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 21:54
"""


from prj_config.prj_process import PrjProcess

if __name__ == "__main__":
    processes = PrjProcess()
    processes.start()
    processes.join()


