#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : ipc_io.py
@Software: PyCharm Community Edition
@Time    : 2018/8/23 21:35
"""

import time


def thread_ipc_receive(my_global):
    print('Thread college ipc receive start..')

    while True:
        print("College get ipc msg from college-------------%s" % str(time.localtime(time.time())))
        ipc_msg = my_global.queues.ipc_rcv_from_college().data
        print(ipc_msg)

    print('Thread college ipc receive stop..')
