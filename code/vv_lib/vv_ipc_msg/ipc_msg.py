#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : ipc_msg.py
@Software: PyCharm Community Edition
@Time    : 2018/8/22 22:16
"""

from enum import Enum, unique

MSG_TYPE = ()


@unique
class ModuleId(Enum):
    ModuleId_College = 1
    ModuleId_Student = 2


@unique
class IpcType(Enum):
    IPC_Type_College = 1
    IPC_Type_Student = 2


@unique
class Opcode(Enum):
    IPC_Opcode_Add = 1
    IPC_Opcode_Del = 2
    IPC_Opcode_Update = 3
    IPC_Opcode_Get = 4
    IPC_Opcode_Getbulk = 5


class IpcMsg:
    """添加类说明"""
    def __init__(self, module_id, sender_id, ipc_type, msg_type, msg_subtype, opcode, data):
        self.module_id = module_id
        self.sender_id = sender_id
        self.ipc_type = ipc_type
        self.msg_type = msg_type
        self.msg_subtype = msg_subtype
        self.opcode = opcode
        self.data = data



