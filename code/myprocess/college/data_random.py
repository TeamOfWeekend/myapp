#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : data_random.py
@site    : 
@Time    : 2018/9/3 16:22
@Software: PyCharm Community Edition
"""

import random

from vv_lib.vv_person.baijiaxing import get_random_name
from vv_lib.vv_college.types import CollegeInformation
from vv_lib.vv_college.college import ImCollege
from vv_lib.vv_college.academy import ImAcademy
from vv_lib.vv_college.major import ImMajor
from vv_lib.vv_college.grade import ImGrade
from vv_lib.vv_college.cclass import ImClass
from vv_lib.vv_college.student import ImStudent
from vv_lib.vv_college.teacher import ImTeacher


COLLEGES_NAME = ['清华大学', '北京大学', '中国人民大学', '北京航空航天大学', '郑州大学']
ACADEMY_MAJORS = {'计算机学院': ['软件工程', '计算机科学与技术', '计算机软件'],
                     '信息工程学院': ['信息工程', '通信工程', '电子信息工程'],
                     '电气工程学院': ['电气工程及其自动化', '自动化', '生物医学工程'],
                     '医学院': ['基础医学', '预防医学', '临床医学', '麻醉学', '医学影像'],
                     '土木工程学院': ['土木工程', '水务工程'],
                     '机械工程学院': ['机械设计制造及自动化', '材料成型机控制工程', '工业设计'],
                     '理学院': ['数学与应用数学', '信息与计算科学', '数理基础科学'],
                     '文学院': ['图书馆学', '档案学', '汉语言文学'],
                     '历史学院': ['历史学', '考古学', '世界历史', '民族学']}

# 每个专业每级班级数的最大最小值
CLASS_PER_MAJOR_MIN = 1
CLASS_PER_MAJOR_MAX = 10

# 每个班学生数量的最大最小值
STUDENTS_PER_CLASS_MAX = 50
STUDENTS_PER_CLASS_MIN = 5

# 每个专业教师数量的最大值和最小值
TEACHERS_PET_MAJOR_MAX = 50
TEACHERS_PET_MAJOR_MIN = 20


def create_random_college_info(gColleges_info):
    """
    创建随机的大学信息
    :param gColleges_info:
    :return:
    """
    if not isinstance(gColleges_info, CollegeInformation):
        raise TypeError('gColleges_info')
    global COLLEGES_NAME, ACADEMY_MAJORS

    for college_name in COLLEGES_NAME:
        gColleges_info.add_college_info(college_name)
        for academy_name in ACADEMY_MAJORS.keys():
            gColleges_info.add_academy_info(college_name, academy_name)
            for major_name in ACADEMY_MAJORS[academy_name]:
                gColleges_info.add_major_info(college_name, academy_name, major_name)
                for grade_id in range(1, 5):
                    gColleges_info.add_grade_info(college_name, academy_name, major_name, grade_id)
                    for class_id in range(1, 5):
                        gColleges_info.add_class_info(college_name, academy_name, major_name, grade_id, class_id)


def create_random_colleges(gColleges_info, gColleges):
    """
    根据随机大学信息，创建随机大学数据
    :param gColleges:
    :param gColleges_info:
    :return:
    """
    if not isinstance(gColleges, list):
        raise TypeError('gColleges')
    if not isinstance(gColleges_info, CollegeInformation):
        raise TypeError('gColleges_info')
    for college_name, college_info in gColleges_info.information.items():
        college = ImCollege()
        college.name = college_name
        gColleges.append(ImCollege())
        for academy_name, academy_info in college_info.items():
            academy = ImAcademy()
            academy.name = academy_name
            college.add_academy(academy)
            for major_name, major_info in academy_info.items():
                major = ImMajor()
                major.name = major_name
                major.teachers = get_random_teachers()
                academy.add_major(major)
                for grade_id, grade_info in major_info.items():
                    grade = ImGrade()
                    grade.id = grade
                    major.add_grade(grade)
                    for class_id in grade_info:
                        cclass = ImClass()
                        cclass.id = class_id
                        cclass.students = get_random_students()
                        cclass.update_student_id()
                        grade.add_class(cclass)


def get_random_teachers():
    rand_int = random.randint(TEACHERS_PET_MAJOR_MIN, TEACHERS_PET_MAJOR_MAX)
    teachers = {}
    for i in range(0, rand_int):
        teacher = ImTeacher()
        teacher.name = get_random_name()
        teachers[teacher.name] = teacher
    return teachers


def get_random_students():
    rand_int = random.randint(STUDENTS_PER_CLASS_MIN, STUDENTS_PER_CLASS_MAX)
    students = {}
    for i in range(0, rand_int):
        student = ImStudent()
        student.name = get_random_name()
        student.id = i + 1
        students[student.name] = student
    return students


colleges_info = CollegeInformation()
create_random_college_info(colleges_info)
print(colleges_info.information)

colleges = []
create_random_colleges(colleges, colleges_info)
for college in colleges:
    print(college.name)
