#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 18:57
# @File    : leetCode_551.py

'''
学生奖励
不超过一个A，和两次L

'''


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count("A") < 2 and "LLL" not in s