#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : test.py
@site    : 
@Time    : 2018/9/8 14:42
@Software: PyCharm Community Edition
"""


from enum import Enum, unique
import numpy as np
import pandas as pd

@unique
class TLV_TAG(Enum):
    STR = 1
    INT = 2


# # 取所有枚举成员的keys、values
# print('keys   : ', TLV_TAG.__members__.keys())
# print('values : ', TLV_TAG.__members__.values())
# print('items  : ', TLV_TAG.__members__.items())
#
# # 取枚举成员数量
# print('length : ', len(TLV_TAG))        # 有警告，但可以用
# print(TLV_TAG.__len__())
#
# # 取值方式
# print(TLV_TAG.INT)
# print(TLV_TAG(2))
# print(TLV_TAG['INT'])
#
# # 判断一个枚举值是否属于该枚举
# print(TLV_TAG.STR in TLV_TAG.__members__.values())
#
# # 判断一个字符串是否属于该枚举的keys，有时需要将枚举与字符串进行转换
# print('INT' in TLV_TAG.__members__.keys())
#
# # 输出一个枚举值的name、value
# print(TLV_TAG.INT.name, ' <----> ', TLV_TAG.INT.value)
#
# # 遍历所有枚举值
# for name, value in TLV_TAG.__members__.items():
#     print(name, ' ==> ', value)
#
#
# print('减肥来得及、绝地反击的、发动机方式'.split('、'))
# print(len(''.split('、')))


class Test:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


def list_all(test):
    for name, value in vars(test).items():
        # test[name] += 1
        print('item  : ', name, value)

    for key in vars(test).keys():
        print('key   : ', key)

    for value in vars(test).values():
        print('value : ', value)

    for x in dir(test):
        print('x : ', x)



# test = Test()
# list_all(test)

def f(string):
    if not isinstance(string, str):
        raise TypeError
    print(string)

# try:
#     f(100)
# except:
#     f('haha')
# else:
#     f('else')
# finally:
#     f('finally')

frame = pd.DataFrame(np.arange(100).reshape(10,10))
print(frame)
