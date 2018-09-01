#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imCollege.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:07
"""

# import random
from vv_lib.vv_college.types import AcademyEnum, CollegeLevel
from vv_lib.vv_college.academy import ImAcademy


class ImCollege():
    """大学"""
    def __init__(self):
        """学校属性"""
        self._name = ''             # 学校名称
        self._id = 0                # 学校名称
        self._description = ''      # 学校简述
        self._address = ''          # 学校地址
        self._level = 0             # 学校级别
        self._area = 0              # 校园面积
        self._headmaster = None    # 校长
        self._academy_num = 0       # 学院数量
        self._major_num = 0         # 专业数量
        self._student_num = 0       # 学生数量
        self._teacher_num = 0       # 教师数量
        self._academy_names = []    # 学院名称列表
        self._academy_dict = {}     # 学院信息字典，key为学院名，value为学院对象

    def to_dict(self):
        """
        将ImCollege实例的属性按顺序放置在字典中
        :return:
        """
        attrs_dict = {}
        attrs_dict['name'] = self.name
        attrs_dict['id'] = self.id
        attrs_dict['description'] = self.description
        attrs_dict['address'] = self.address
        attrs_dict['level'] = self.level
        attrs_dict['area'] = self.area
        attrs_dict['academy_num'] = self.academy_num
        attrs_dict['academy_names'] = self.academy_names
        return attrs_dict

    def fill_attrs(self, attrs):
        """
        向ImCollege实例中添加属性，attrs是字典
        :param attrs:  包含属性的字典
        :return:
        """
        if not isinstance(attrs, dict):
            raise TypeError('attrs must be type of dict')


    def createRandomAttrs(self):
        """生成随机属性"""
        # self.id = random.randint(1, len(CollegeEnum))
        # self.name = CollegeEnum(self.id).name
        for academyE in AcademyEnum:
            academy = ImAcademy(self, academyE.value)
            academy.fillMajors()
            self.academies[academyE.name] = academy
            self.academyNum += 1
        # print('--------------------------------------')
        # for key, val in self.academies.items():
        #     print(key)
        #     print(val.majors.keys())
        # print(self.getStudentNum())


    def getStudentNum(self):
        """获取全校学生数量"""
        stuNum = 0
        for academy in self.academies.values():
            for major in academy.majors.values():
                for grade in major.grades:
                    for classs in grade.classes:
                        stuNum += len(classs.students)
        return stuNum

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('college name must be type of str')
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('college id must be type of int')
        self._id = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError('college description must be type of str')
        self._description = description

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise TypeError('college address must be type of str')
        self._address = address

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level not in CollegeLevel.__members__.values():
            raise TypeError('college address must be member of CollegeLevel')
        self._level = level

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, val):
        if not isinstance(val, int):
            raise TypeError('area must be type of int')
        self._area = val

    @property
    def academy_num(self):
        return self._academy_num

    @academy_num.setter
    def academy_num(self, val):
        if not isinstance(val, int):
            raise TypeError('academy num must be type of int')
        self._academy_num = val

    @property
    def academy_names(self):
        return self._academy_names

    @academy_names.setter
    def academy_names(self, names):
        if not isinstance(names, list):
            raise TypeError('academy names must be type of list')
        self._academy_names = names

    @property
    def academy_dict(self):
        return self._academy_dict

    @academy_dict.setter
    def academy_dict(self, academys):
        if not isinstance(academys, dict):
            raise TypeError('academys must be type of dict')
        self._academy_dict = academys


a = {1:11, 2:22}
a[3]
