#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : data_api.py
@Software: PyCharm Community Edition
@Time    : 2018/8/30 22:26
"""

from vv_lib.vv_college.m_college import ImCollege
from vv_lib.vv_college.m_academy import ImAcademy
from vv_lib.vv_college.m_major import ImMajor
from vv_lib.vv_college.m_grade import ImGrade
from vv_lib.vv_college.m_class import ImClass
from vv_lib.vv_college.m_student import ImStudent


def add_college(colleges, college):
    """
    向colleges数据库中添加一项college数据
    :param colleges:
    :param college:
    :return:
    """
    if not isinstance(colleges, list) or isinstance(college, ImCollege):
        raise TypeError('colleges must be a list, college must be a sample of ImCollege')
    colleges.append(college)


def get_college(colleges, college_name):
    """
    从colleges数据库中获取一项college数据
    :param colleges:
    :param college_name:
    :return:
    """
    for college in colleges:
        if college_name == college.name:
            return college
    return None


def add_academy(colleges, college_name, academy):
    """
    向学校中添加一项学院数据
    :param colleges:
    :param college_name:
    :param academy: sample of ImAcademy
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy, ImAcademy):
        raise TypeError('academy')
    college = get_college(colleges, college_name)
    college.add_academy(academy.name)


def get_academy(colleges, college_name, academy_name):
    """
    根据学校、学院名称获取学院信息
    :param colleges:
    :param college_name:
    :param academy_name:
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy_name, str):
        raise TypeError('academy_name')
    college = get_college(colleges, college_name)
    return college.get_academy(academy_name)


def add_major(colleges, college_name, academy_name, major):
    """
    根据学校、学院名称、专业名称获取专业信息
    :param colleges:
    :param college_name:
    :param academy_name:
    :param major:
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy_name, str):
        raise TypeError('academy_name')
    if not isinstance(major, ImMajor):
        raise TypeError('major')
    academy = get_academy(colleges, college_name, academy_name)
    academy.add_major(major)


def get_major(colleges, college_name, academy_name, major_name):
    """
    根据学校、学院名称、专业名称获取专业信息
    :param colleges:
    :param college_name:
    :param academy_name:
    :param major_name:
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy_name, str):
        raise TypeError('academy_name')
    if not isinstance(major_name, str):
        raise TypeError('major_name')
    academy = get_academy(colleges, college_name, academy_name)
    return academy.get_major(major_name)


def add_grade(colleges, college_name, academy_name, major_name, grade):
    """
    根据学校、学院名称、专业、年级号名称获取年级信息
    :param colleges:
    :param college_name:
    :param academy_name:
    :param major_name:
    :param grade:
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy_name, str):
        raise TypeError('academy_name')
    if not isinstance(major_name, str):
        raise TypeError('major_name')
    if not isinstance(grade, ImGrade):
        raise TypeError('grade')
    major = get_major(colleges, college_name, academy_name, major_name)
    major.add_grade(grade)


def get_grade(colleges, college_name, academy_name, major_name, grade_id):
    """
    根据学校、学院名称、专业、年级号名称获取年级信息
    :param colleges:
    :param college_name:
    :param academy_name:
    :param major_name:
    :param grade_id:
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy_name, str):
        raise TypeError('academy_name')
    if not isinstance(major_name, str):
        raise TypeError('major_name')
    if not isinstance(grade_id, int):
        raise TypeError('grade_id')
    major = get_major(colleges, college_name, academy_name, major_name)
    return major.get_grade(grade_id)


def add_classs(colleges, college_name, academy_name, major_name, grade_id, classs):
    """
    根据学校、学院名称、专业名称、年级号、班级号获取班级信息
    :param colleges:
    :param college_name:
    :param academy_name:
    :param major_name:
    :param grade_id:
    :param classs:
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy_name, str):
        raise TypeError('academy_name')
    if not isinstance(major_name, str):
        raise TypeError('major_name')
    if not isinstance(grade_id, int):
        raise TypeError('grade_id')
    if not isinstance(classs, ImClass):
        raise TypeError('classs')
    grade = get_grade(colleges, college_name, academy_name, major_name, grade_id)
    grade.add_class(classs)


def get_classs(colleges, college_name, academy_name, major_name, grade_id, class_id):
    """
    根据学校、学院名称、专业名称、年级号、班级号获取班级信息
    :param colleges:
    :param college_name:
    :param academy_name:
    :param major_name:
    :param grade_id:
    :param class_id:
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy_name, str):
        raise TypeError('academy_name')
    if not isinstance(major_name, str):
        raise TypeError('major_name')
    if not isinstance(grade_id, int):
        raise TypeError('grade_id')
    if not isinstance(class_id, int):
        raise TypeError('class_id')
    grade = get_grade(colleges, college_name, academy_name, major_name, grade_id)
    return grade.get_class(class_id)


def add_student(colleges, college_name, academy_name, major_name, grade_id, class_id, student):
    """
    根据学校、学院名称、专业名称、年级号、班级号、学号获取学生信息
    :param colleges:
    :param college_name:
    :param academy_name:
    :param major_name:
    :param grade_id:
    :param class_id:
    :param student:
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy_name, str):
        raise TypeError('academy_name')
    if not isinstance(major_name, str):
        raise TypeError('major_name')
    if not isinstance(grade_id, int):
        raise TypeError('grade_id')
    if not isinstance(class_id, int):
        raise TypeError('class_id')
    if not isinstance(student, ImStudent):
        raise TypeError('student')
    classs = get_classs(colleges, college_name, academy_name, major_name, grade_id, class_id)
    classs.add_student(student)


def get_student(colleges, college_name, academy_name, major_name, grade_id, class_id, student_id):
    """
    根据学校、学院名称、专业名称、年级号、班级号、学号获取学生信息
    :param colleges:
    :param college_name:
    :param academy_name:
    :param major_name:
    :param grade_id:
    :param class_id:
    :param student_id:
    :return:
    """
    if not isinstance(colleges, list):
        raise TypeError('colleges')
    if not isinstance(college_name, str):
        raise TypeError('college_name')
    if not isinstance(academy_name, str):
        raise TypeError('academy_name')
    if not isinstance(major_name, str):
        raise TypeError('major_name')
    if not isinstance(grade_id, int):
        raise TypeError('grade_id')
    if not isinstance(class_id, int):
        raise TypeError('class_id')
    if not isinstance(student_id, int):
        raise TypeError('student_id')
    classs = get_classs(colleges, college_name, academy_name, major_name, grade_id, class_id)
    return classs.get_student(student_id)

