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
    Django = 1
    College = 2
    Student = 3


@unique
class IPC_Type(Enum):
    College = 1
    Academy = 2
    Major = 3
    Grade = 4
    Classs = 5
    Student = 6


@unique
class IPC_Opcode(Enum):
    Add = 1
    Del = 2
    Update = 3
    Get = 4
    Getbulk = 5


@unique
class TLV_TAG(Enum):
    STR = 1
    INT = 2



class TLV():
    """tag、length、value数据结构"""
    def __init__(self, tag, length, value):
        """
        :param tag: 从枚举类TLV_TAG中选择
        :param length: >1
        :param value: 列表或字符串
        """
        if tag not in TLV_TAG.__members__.values():
            raise TypeError('tag must be a member of TLV_TAG')
        if length < 1:
            raise ValueError('length must be > 1')
        if not isinstance(value, str) or not isinstance(value, list):
            raise TypeError("value's type must be str or list")

        self.tag = tag
        self.length = length
        self.value = value


class IpcMsg:
    """添加类说明"""
    def __init__(self, module_id=0, sender_id=0, ipc_type=0, msg_type=0, msg_subtype=0, opcode=0):
        self.module_id = module_id
        self.sender_id = sender_id
        self.ipc_type = ipc_type
        self.msg_type = msg_type
        self.msg_subtype = msg_subtype
        self.opcode = opcode
        self.data_len = 0
        self.data = []

    # 增加数据，必须是TLV格式
    def data_add(self, tlv):
        if not isinstance(tlv, TLV):
            raise TypeError("tlv must be a sample of TLV")
        self.data[self.data_len:(self.data_len + 1)] = tlv.tag
        self.data_len += 1
        self.data[self.data_len:(self.data_len + 1)] = tlv.length
        self.data_len += 1
        self.data[self.data_len:(self.data_len + 1)] = tlv.value
        self.data_len += tlv.length



