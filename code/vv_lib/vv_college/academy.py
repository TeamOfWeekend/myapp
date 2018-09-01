#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imAcademy.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:29
"""

from vv_lib.vv_college.types import ACADEMY_MAJOR_DIR, AcademyEnum
from vv_lib.vv_college.major import ImMajor
from vv_lib.vv_college.college import ImCollege


class ImAcademy:
    """学院"""
    def __init__(self, college=None, mid=0):
        self._name = ''             # 名称
        self._id = mid              # 编号
        self._description = ''      # 学院概述
        self._major_num = 0         # 专业数量
        self._major_names = []      # 专业名称
        self._majors = {}           # 专业
        self._college = college     # 所属学校

    def fillMajors(self):
        # try:
        self.name = AcademyEnum(self.id).name
        for id in range(0, len(ACADEMY_MAJOR_DIR[self.name])):
            major = ImMajor(self, id+1)
            major.name = ACADEMY_MAJOR_DIR[self.name][id]
            major.createRandomAttrs()
            self.majors[ACADEMY_MAJOR_DIR[self.name][id]] = major
            self.major_num += 1
        # except:
        #     print('选择的院系名称有误')

    def add_major(self, major):
        if not isinstance(major, ImMajor):
            raise TypeError('major')
        if major.name not in self.majors.keys():
            self.majors[major.name] = major

    def del_major(self, major_name):
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if major_name in self.majors.keys():
            del self.majors[major_name]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name')
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('id')
        self._id = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError('description')
        self._description = description

    @property
    def major_num(self):
        return self._major_num

    @major_num.setter
    def major_num(self, val):
        if not isinstance(val, int):
            raise TypeError('major_num')
        self._major_num = val

    @property
    def major_names(self):
        return self._major_names

    @major_names.setter
    def major_names(self, major_names):
        if not isinstance(major_names, list):
            raise TypeError('major_names')
        self._major_names = major_names

    @property
    def majors(self):
        return self._majors

    @majors.setter
    def majors(self, majors):
        if not isinstance(majors, dict):
            raise TypeError('major_dict')
        self._majors = majors

    @property
    def college(self):
        return self._college

    @college.setter
    def college(self, college):
        if not isinstance(college, ImCollege):
            raise TypeError('college')
        self._college = college
