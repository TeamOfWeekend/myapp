#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : ipc_api.py
@Software: PyCharm Community Edition
@Time    : 2018/8/30 22:28
"""

from vv_lib.vv_ipc_msg.ipc_msg import MSG_Type, IPC_Opcode, IpcMsg
from myprocess.college.data_api import get_college, get_academy, get_major, get_grade, get_classs, get_student


def handle_ipc_msg(server, data, colleges):
    """
    处理ipc 消息
    :param data: 接收的数据
    :return:
    """
    # print(eval(data.decode()))
    # server.sendall(repr({'college_name' : '北京大学',
    #                      'college_area': 100}).encode())

    ipc_msg = IpcMsg()
    ipc_msg.fill_all(data)

    if MSG_Type.College == ipc_msg.msg_type:
        handle_ipc_msg_college(server, colleges, ipc_msg)
    elif MSG_Type.Academy == ipc_msg.msg_type:
        handle_ipc_msg_academy(server, colleges, ipc_msg)
    elif MSG_Type.Major == ipc_msg.msg_type:
        handle_ipc_msg_major(server, colleges, ipc_msg)
    elif MSG_Type.Grade == ipc_msg.msg_type:
        handle_ipc_msg_grade(server, colleges, ipc_msg)
    elif MSG_Type.Classs == ipc_msg.msg_type:
        handle_ipc_msg_classs(server, colleges, ipc_msg)
    elif MSG_Type.Student == ipc_msg.msg_type:
        handle_ipc_msg_student(server, colleges, ipc_msg)

    college_name = data['college_name']
    print(college_name)
    # server.sendall(str({'college_name': '北京大学',
    #                      'college_area': 100}).encode())
    server.sendall(repr(get_college(colleges, college_name)).encode())


def handle_ipc_msg_college(server, colleges, ipc_msg):
    """
    处理college类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    college_name = ipc_msg.data['college_name']
    return get_college(colleges, college_name)


def handle_ipc_msg_academy(server, colleges, ipc_msg):
    """
    处理academy类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    college_name = ipc_msg.data['college_name']
    academy_name = ipc_msg.data['academy_name']
    college = get_college(colleges, college_name)
    return get_academy(college, academy_name)


def handle_ipc_msg_major(server, colleges, ipc_msg):
    """
    处理major类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    pass


def handle_ipc_msg_grade(server, colleges, ipc_msg):
    """
    处理grade类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    pass


def handle_ipc_msg_classs(server, colleges, ipc_msg):
    """
    处理classs类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    pass


def handle_ipc_msg_student(server, colleges, ipc_msg):
    """
    处理student类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    pass
