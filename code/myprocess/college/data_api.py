#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : data_api.py
@Software: PyCharm Community Edition
@Time    : 2018/8/30 22:26
"""


def get_college(colleges, college_name):
    for college in colleges:
        if college_name == college.name:
            return college
    return None


def get_academy(college, academy_name):
    """
    根据学校、学院名称获取学院信息
    :param college:
    :param academy_name:
    :return:
    """
    pass


def get_major(college, academy_name, major_name):
    """
    根据学校、学院名称、专业名称获取专业信息
    :param college:
    :param academy_name:
    :param major_name:
    :return:
    """
    pass


def get_grade(college, academy_name, major_name, grade_id):
    """
    根据学校、学院名称、专业、年级号名称获取年级信息
    :param college:
    :param academy_name:
    :param major_name:
    :param grade_id:
    :return:
    """
    pass



def get_classs(college, academy_name, major_name, grade_id, class_id):
    """
    根据学校、学院名称、专业名称、年级号、班级号获取班级信息
    :param college:
    :param academy_name:
    :param major_name:
    :param grade_id:
    :param class_id:
    :return:
    """
    pass


def get_student(college, academy_name, major_name, grade_id, class_id, student_id):
    """
    根据学校、学院名称、专业名称、年级号、班级号、学号获取学生信息
    :param college:
    :param academy_name:
    :param major_name:
    :param grade_id:
    :param class_id:
    :param student_id:
    :return:
    """
    pass

