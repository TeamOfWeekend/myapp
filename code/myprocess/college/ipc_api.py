#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : ipc_api.py
@Software: PyCharm Community Edition
@Time    : 2018/8/30 22:28
"""

import json
from vv_lib.vv_ipc_msg.ipc_msg import MSG_Type, IPC_Opcode, IpcMsg
from .data_api import get_college, get_academy, get_major, get_grade, get_classs, get_student


def handle_ipc_msg(server, data, colleges):
    """
    处理ipc消息
    :param server:
    :param data:
    :param colleges:
    :return:
    """
    ipc_msg = IpcMsg()
    # ipc_msg.fill_all(eval(data.decode()))
    ipc_msg.fill_all(json.loads(data.decode()))

    print('recv socket msg : ', ipc_msg.msg_type)

    if MSG_Type.All_Colleges == ipc_msg.msg_type:
        handle_ipc_msg_all_colleges(server, colleges, ipc_msg)
    elif MSG_Type.College == ipc_msg.msg_type:
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


def handle_ipc_msg_all_colleges(server, colleges, ipc_msg):
    """
    处理college类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    if IPC_Opcode.Get == ipc_msg.opcode:
        if 0 == colleges.colleges_num:
            send_ipc_no_reply(server, ipc_msg)
        else:
            data = colleges.to_dict()
            send_ipc_reply(server, ipc_msg, data)


def handle_ipc_msg_college(server, colleges, ipc_msg):
    """
    处理college类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    if IPC_Opcode.Get == ipc_msg.opcode:
        college_name = ipc_msg.data['college_name']
        college = colleges.get_college(college_name)
        if college is None:
            send_ipc_no_reply(server, ipc_msg)
        else:
            data = college.to_dict()
            send_ipc_reply(server, ipc_msg, data)


def handle_ipc_msg_academy(server, colleges, ipc_msg):
    """
    处理academy类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    college_name = ipc_msg.data['college_name']
    academy_name = ipc_msg.data['academy_name']
    academy = colleges.get_academy(college_name, academy_name)
    if academy is None:
        send_ipc_no_reply(server, ipc_msg)
    else:
        data = academy.to_dict()
        send_ipc_reply(server, ipc_msg, data)


def handle_ipc_msg_major(server, colleges, ipc_msg):
    """
    处理major类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    college_name = ipc_msg.data['college_name']
    academy_name = ipc_msg.data['academy_name']
    major_name = ipc_msg.data['major_name']
    major = colleges.get_major(college_name, academy_name, major_name)
    if major is None:
        send_ipc_no_reply(server, ipc_msg)
    else:
        data = major.to_dict()
        send_ipc_reply(server, ipc_msg, data)


def handle_ipc_msg_grade(server, colleges, ipc_msg):
    """
    处理grade类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    college_name = ipc_msg.data['college_name']
    academy_name = ipc_msg.data['academy_name']
    major_name = ipc_msg.data['major_name']
    grade_id = ipc_msg.data['grade_id']
    grade = colleges.get_grade(college_name, academy_name, major_name, grade_id)
    print(grade_id, grade, type(grade))
    if grade is None:
        send_ipc_no_reply(server, ipc_msg)
    else:
        data = grade.to_dict()
        print(data)
        send_ipc_reply(server, ipc_msg, data)


def handle_ipc_msg_classs(server, colleges, ipc_msg):
    """
    处理classs类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    college_name = ipc_msg.data['college_name']
    academy_name = ipc_msg.data['academy_name']
    major_name = ipc_msg.data['major_name']
    grade_id = ipc_msg.data['grade_id']
    class_id = ipc_msg.data['class_id']
    cclass = colleges.get_classs(college_name, academy_name, major_name, grade_id, class_id)
    if cclass is None:
        send_ipc_no_reply(server, ipc_msg)
    else:
        data = cclass.to_dict()
        send_ipc_reply(server, ipc_msg, data)


def handle_ipc_msg_student(server, colleges, ipc_msg):
    """
    处理student类型的ipc消息
    :param server:
    :param colleges:
    :return:
    """
    college_name = ipc_msg.data['college_name']
    academy_name = ipc_msg.data['academy_name']
    major_name = ipc_msg.data['major_name']
    grade_id = ipc_msg.data['grade_id']
    class_id = ipc_msg.data['class_id']
    student_id = ipc_msg.data['student_id']
    student = colleges.get_student(college_name, academy_name, major_name, grade_id, class_id, student_id)
    if student is None:
        send_ipc_no_reply(server, ipc_msg)
    else:
        data = student.to_dict()
        send_ipc_reply(server, ipc_msg, data)


def send_ipc_reply(server, ipc_msg_rcv, data):
    """
    发送ipc应答消息
    :param server: socket server or connect
    :param ipc_msg_rcv:  接收的ipc消息
    :param data: 要发送的数据
    :return:
    """
    ipc_msg_send = IpcMsg()
    ipc_msg_send.module_id = ipc_msg_rcv.sender_id
    ipc_msg_send.sender_id = ipc_msg_rcv.module_id
    ipc_msg_send.msg_type = ipc_msg_rcv.msg_type
    ipc_msg_send.msg_subtype = ipc_msg_rcv.msg_subtype
    ipc_msg_send.opcode = IPC_Opcode.Reply
    ipc_msg_send.data = data
    # server.sendall(repr(ipc_msg_send.to_list()).encode())
    server.sendall(json.dumps(ipc_msg_send.to_list()).encode())


def send_ipc_no_reply(server, ipc_msg_rcv):
    """
    发送非应答消息，即无数据
    :param server:
    :param ipc_msg_rcv:
    :return:
    """
    ipc_msg_send = IpcMsg()
    ipc_msg_send.module_id = ipc_msg_rcv.sender_id
    ipc_msg_send.sender_id = ipc_msg_rcv.module_id
    ipc_msg_send.msg_type = ipc_msg_rcv.msg_type
    ipc_msg_send.msg_subtype = ipc_msg_rcv.msg_subtype
    ipc_msg_send.opcode = IPC_Opcode.NoReply
    # server.sendall(repr(ipc_msg_send.to_list()).encode())
    server.sendall(json.dumps(ipc_msg_send.to_list()).encode())
