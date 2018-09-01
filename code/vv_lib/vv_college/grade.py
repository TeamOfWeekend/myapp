#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imGrade.py
@site    : 
@Time    : 2018/7/25 10:09
@Software: PyCharm Community Edition
"""

import random

from vv_lib.vv_college.types import CLASSS_IN_MAJOR_MIN, CLASSS_IN_MAJOR_MAX
from vv_lib.vv_college.cclass import ImClass
from vv_lib.vv_college.major import ImMajor


class ImGrade:
    """年级类"""
    def __init__(self):
        self._id = 0            # 年级编号
        self._class_num = 0     # 包含的班级数量
        self._classes = {}      # 存放班级的字典
        self._major = None     # 所属的专业


    def createRandomAttrs(self):
        """创建随机属性"""
        self._class_num = random.randint(CLASSS_IN_MAJOR_MIN, CLASSS_IN_MAJOR_MAX)
        for i in range(0, self._class_num):
            classs = ImClass(self, i+1)
            classs.createRandomAttrs()
            self.add_class(classs)

    def add_class(self, classs):
        if not isinstance(classs, ImClass):
            raise TypeError('classs')
        if classs.id not in self.classes.keys():
            self.classes[classs.id] = classs

    def del_class(self, class_id):
        if not isinstance(class_id, int):
            raise TypeError('class_id')
        if class_id not in self.classes.keys():
            del self.classes[class_id]

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('val')
        self._id = val

    @property
    def class_num(self):
        return self._class_num

    @property
    def classes(self):
        return self._classes

    @classes.setter
    def classes(self, classes):
        if not isinstance(classes, dict):
            raise TypeError('classes')
        self._classes = classes

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        if not isinstance(major, ImMajor):
            raise TypeError('major')
        self._major = major
