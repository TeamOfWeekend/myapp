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
import pandas as pd


from vv_lib.vv_person.baijiaxing import get_random_name
from vv_lib.vv_college.m_types import CollegeInformation
from vv_lib.vv_college.m_colleges import ImColleges
from vv_lib.vv_college.m_college import ImCollege, CollegeLevel
from vv_lib.vv_college.m_academy import ImAcademy
from vv_lib.vv_college.m_major import ImMajor
from vv_lib.vv_college.m_grade import ImGrade
from vv_lib.vv_college.m_class import ImClass
from vv_lib.vv_college.m_student import ImStudent
from vv_lib.vv_college.m_teacher import ImTeacher



ACADEMY_MAJORS = {'计算机学院': ['软件工程', '计算机科学与技术', '计算机软件'],
                     '信息工程学院': ['信息工程', '通信工程', '电子信息工程'],
                     '电气工程学院': ['电气工程及其自动化', '自动化', '生物医学工程'],
                     '医学院': ['基础医学', '预防医学', '临床医学', '麻醉学', '医学影像'],
                     '土木工程学院': ['土木工程', '水务工程'],
                     '机械工程学院': ['机械设计制造及自动化', '材料成型机控制工程', '工业设计'],
                     '理学院': ['数学与应用数学', '信息与计算科学', '数理基础科学'],
                     '文学院': ['图书馆学', '档案学', '汉语言文学'],
                     '历史学院': ['历史学', '考古学', '世界历史', '民族学']}

COLLEGES_INFO = {'清华大学': {'name': '清华大学', 'id': 10003, 'description': '', 'birthday': '1911/4/26',
                          'address': '北京市海淀区清华大学', 'level': CollegeLevel.双一流, 'area': 5000,
                          'headmaster': '邱勇'},
                 '北京大学': {'name': '北京大学', 'id': 10001, 'description': '', 'birthday': '1898/7/3',
                          'address': '北京市海淀区颐和园路5号', 'level': CollegeLevel.双一流, 'area': 5000,
                          'headmaster': '林建华'},
                 '中国人民大学': {'name': '中国人民大学', 'id': 10002, 'description': '', 'birthday': '1937/10/3',
                            'address': '北京市海淀区中关村大街59号', 'level': CollegeLevel.双一流, 'area': 5000,
                            'headmaster': '刘伟'},
                 '北京航空航天大学': {'name': '北京航空航天大学', 'id': 10006, 'description': '', 'birthday': '1952/10/25',
                              'address': '北京市海淀区学院路37号', 'level': CollegeLevel.双一流, 'area': 3000,
                              'headmaster': '徐惠彬'},
                 '郑州大学': {'name': '郑州大学', 'id': 10459, 'description': '', 'birthday': '1954/9/15',
                          'address': '郑州市高新技术开发区科学大道100号', 'level': CollegeLevel.双一流, 'area': 5700,
                          'headmaster': '刘炯天'},
                 }

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
    global COLLEGES_INFO, ACADEMY_MAJORS

    for college_name in COLLEGES_INFO.keys():
        gColleges_info.add_college_info(college_name)
        for academy_name in ACADEMY_MAJORS.keys():
            gColleges_info.add_academy_info(college_name, academy_name)
            for major_name in ACADEMY_MAJORS[academy_name]:
                gColleges_info.add_major_info(college_name, academy_name, major_name)
                for grade_id in range(1, 5):
                    gColleges_info.add_grade_info(college_name, academy_name, major_name, grade_id)
                    for class_id in range(1, 5):
                        gColleges_info.add_class_info(college_name, academy_name, major_name, grade_id, class_id)


def create_random_colleges(gColleges):
    """
    根据随机大学信息，创建随机大学数据
    :param gColleges:
    :param gColleges_info:
    :return:
    """
    global COLLEGES_INFO, ACADEMY_MAJORS
    if not isinstance(gColleges, ImColleges):
        raise TypeError('gColleges')
    for college_name, college_info in COLLEGES_INFO.items():
        college = ImCollege()
        college.name = college_name
        college.id = college_info['id']
        college.description = college_info['description']
        college.address = college_info['address']
        college.level = college_info['level']
        college.area = college_info['area']
        college.headmaster.name = college_info['headmaster']
        college.birthday = college_info['birthday']
        print('college name : %s' % college.name)
        gColleges.add_college(college)
        for academy_name, academy_info in ACADEMY_MAJORS.items():
            academy = ImAcademy()
            academy.name = academy_name
            academy.college = college
            for major_name in academy_info:
                major = ImMajor()
                major.name = major_name
                major.academy = academy
                teachers = get_random_teachers()
                for teacher in teachers:
                    major.add_teacher(teacher)
                for grade_id in range(1, 5):
                    grade = ImGrade()
                    grade.id = grade_id
                    grade.major = major
                    for class_id in range(1, 5):
                        cclass = ImClass()
                        cclass.id = class_id
                        cclass.grade = grade
                        students = get_random_students(cclass)
                        for student in students:
                            cclass.add_student(student)

                        cclass.update_student_id()
                        grade.add_class(cclass)
                    major.add_grade(grade)
                academy.add_major(major)
            college.add_academy(academy)


def get_random_teachers():
    rand_int = random.randint(TEACHERS_PET_MAJOR_MIN, TEACHERS_PET_MAJOR_MAX)
    teachers = []
    for i in range(0, rand_int):
        teacher = ImTeacher()
        teacher.name = get_random_name()
        teachers.append(teacher)
    return teachers


def get_random_students(cclass):
    rand_int = random.randint(STUDENTS_PER_CLASS_MIN, STUDENTS_PER_CLASS_MAX)
    students = []
    for i in range(0, rand_int):
        student = ImStudent()
        student.name = get_random_name()
        student.id = i + 1
        student.cclass = cclass
        students.append(student)
    return students


# colleges_info = CollegeInformation()
# create_random_college_info(colleges_info)
# print(colleges_info.information)
#
# g_Colleges = ImColleges()
# create_random_colleges(colleges_info, g_Colleges)
# print(g_Colleges.colleges)
# for college_name in g_Colleges.colleges_name:
#     print(college_name)
