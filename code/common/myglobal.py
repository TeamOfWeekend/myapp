#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : process.py
@Software: PyCharm Community Edition
@Time    : 2018/8/21 21:59
"""

import multiprocessing

from vv_lib.vv_queue.vqueue import VQueue

# 队列编号、名称、大小
queue_def = ((1, 'college queue', 20),
             (2, 'student queue', 20))


class MyQueues():
    def __init__(self):
        self.queues = []
        context = multiprocessing.get_context('spawn')
        for q in queue_def:
            self.queues.append(VQueue(q[0], q[1], q[2], context))


    # 每添加一个队列，添加一对send、recv方法
    # 向队列发送消息
    def ipc_snd_to_college(self, data):
        self.queues[0].put(data)


    # 从队列接收消息
    def ipc_rcv_from_college(self):
        return self.queues[0].get()


    # 向队列发送消息
    def ipc_snd_to_student(self, data):
        self.queues[1].put(data)


    # 从队列接收消息
    def ipc_rcv_from_student(self):
        return self.queues[1].get()


class MyGlobal():
    def __init__(self):
        self.queues = MyQueues()

