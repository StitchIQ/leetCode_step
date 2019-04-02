#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 17:31

# @File    : leetCode_202.py

'''
判断数各个位平方和能否等于1
使用字典来记录数字，如果平方和数字在字典中，则说明开始循环了，
不会等于1了

'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        num = n
        res = dict()
        while num != 1:
            s = 0
            while num > 0:
                t = num % 10
                s += t * t
                num = num // 10
            num = s
            if s in res:
                return False
            res[s] = s
            print("s", num)
        return num == 1

s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
print(s.isHappy(7))