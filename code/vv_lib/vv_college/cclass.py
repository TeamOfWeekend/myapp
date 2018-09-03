#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imClass.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:16
"""

from vv_lib.vv_college.student import ImStudent
from vv_lib.vv_college.grade import ImGrade


class ImClass:
    """大学班级"""
    def __init__(self):
        self._id = id            # 编号
        self._student_num = 0    # 学生数量
        self._students = {}      # 学生
        self._grade = None       # 所属年级

    def update_student_id(self):
        """按名字顺序对学生进行排序"""
        n = len(self.students)
        while n > 1:
            swapped = False
            i = 0
            while i < (n - 1):
                # print("%s  %s" %(self.students[i].name, self.students[i+1].name))
                # print(self.students[i].name < self.students[i+1].name)
                if self.students[i].namePinYin > self.students[i+1].namePinYin:
                    self.students[i], self.students[i+1] = self.students[i+1], self.students[i]
                    swapped = True
                i += 1
            if False == swapped:
                break
            n -= 1

        for i in range(0, len(self.students)):
            self.students[i].id = i + 1
            self.students[i].createId()

    def add_student(self, student):
        if not isinstance(student, ImStudent):
            raise TypeError('student')
        self._student_num += 1
        student.id = self.student_num
        self.students[student.id] = student

    def del_student(self, student_id):
        if not isinstance(student_id, int):
            raise TypeError('student_id')
        if student_id in self.students.keys():
            self._student_num -= 1
            del self.students[student_id]

    def get_student(self, student_name):
        """
        根据学生姓名获取学生对象
        :param student_name:
        :return:
        """
        if not isinstance(student_name, str):
            raise TypeError('student_name')
        if student_name in self.students.keys():
            return self.students[student_name]
        else:
            return None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('val')
        self._id = val

    @property
    def student_num(self):
        return self._student_num

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, students):
        if not isinstance(students, dict):
            raise TypeError('students')
        self._students = students

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if not isinstance(grade, ImGrade):
            raise TypeError('grade')
        self._grade = grade
