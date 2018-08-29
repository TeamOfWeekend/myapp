#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : main_college.py
@Software: PyCharm Community Edition
@Time    : 2018/8/20 21:38
"""

import time

from vv_lib.vv_ipc_msg.ipc_msg import IpcMsg


def run_student(my_global):
    print("Process student start...")

    while True:
        # print("Student put ipc msg to college")
        # ipc_msg1 = IpcMsg(0,0,0,0,0,0,1)
        # my_global.queues.ipc_snd_to_college(ipc_msg1)
        #
        # ipc_msg2 = IpcMsg(0, 0, 0, 0, 0, 0, 2.1)
        # my_global.queues.ipc_snd_to_college(ipc_msg2)
        #
        # ipc_msg3 = IpcMsg(0, 0, 0, 0, 0, 0, 'fjdslfjdslj')
        # my_global.queues.ipc_snd_to_college(ipc_msg3)
        #
        # ipc_msg4 = IpcMsg(0, 0, 0, 0, 0, 0, ['fjdslfjdslj', 1, 1.55, True])
        # my_global.queues.ipc_snd_to_college(ipc_msg4)
        time.sleep(2)
    # while not queue.empty():
    #     print((my_global.ipc_rcv_from_college()).data)
    print("Process student stop...")