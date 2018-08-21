#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : queue.py
@Software: PyCharm Community Edition
@Time    : 2018/8/21 22:02
"""

import multiprocessing

from vv_lib.vv_queue.vqueue import VQueue

# 队列编号、名称、大小
queue_def = ((1, 'send queue', 20),
             (2, 'recv queue', 20))


class PrjQueue:
    """添加类说明"""

    # Constructor
    def __init__(self):
        """Set the initial state of self, which includes the contents of
        sourceCollection, if it's present"""
        self._count = len(queue_def)
        self._queues = []

        ctx = multiprocessing.get_context('spawn')
        for q in queue_def:
            self._queues.append(VQueue(q[0], q[1], q[2], ctx))

    @property
    def count(self):
        return self._count

    @property
    def queues(self):
        return self._queues
