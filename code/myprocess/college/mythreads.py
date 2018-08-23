#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : threads_IO.py
@Software: PyCharm Community Edition
@Time    : 2018/8/23 21:25
"""

import threading

# 线程1：与django服务器进行通信，为django服务器提供数据
# 线程2：college数据更新
# 线程3：与本工程中其他进程通信

from myprocess.college.socket_io import thread_socket_receive
from myprocess.college.data_update import thread_data_update
from myprocess.college.ipc_io import thread_ipc_receive

thread_info = ((1, 'socket with django', thread_socket_receive),
              (2, 'college data update', thread_data_update),
              (3, 'ipc with other process', thread_ipc_receive))


lock_data = threading.Lock()


threads = []
for t in thread_info:
    threads.append(threading.Thread(target=t[2]))




