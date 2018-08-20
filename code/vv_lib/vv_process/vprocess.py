#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : vprocess.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 20:55
"""

from multiprocessing import Process
from queue import Queue
from inspect import isfunction

# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)


class VProcess(Process):
    """添加类说明"""

    # Constructor
    def __init__(self, myid, name, func, queues):
        """Set the initial state of self, which includes the contents of
        sourceCollection, if it's present
        name : 进程名
        func : 进程代码入口
        queue : 进程通信队列"""
        super(VProcess, self).__init__(target=func)
        if not isinstance(myid, int):
            raise TypeError('Process id must be int type')
        if not isinstance(name, str):
            raise TypeError('Process name must be str type')
        # if not isinstance(queue, Queue):
        #     raise TypeError('Process func must be Queue type')
        self.myid = myid
        self.name = name
        self.queues = queues

    def __str__(self):
        """返回进程名字"""
        return self.name

