#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 10:21

# @File    : leetCode_263.py

'''
数字的分解的因子只包含，2，3，5为 ugly数字。
1 定义为 ugly数字。

思路：
循环模 2，3，5，如果不等于0，则为false。
除完后，判断最后的值是否在 2，3，5，或者等于1

思路2：
num分别对2，3，5 取模，直到把等于0，
最后判断是否等于1
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        element = set([2, 3, 5])
        while num > 1:
            t = num
            for e in element:
                if num % e == 0:
                    num /= e
            else:
                if t == num:
                    return False
            # print(num)
        return num in element or num == 1

    def s2(self, num):
        if num <= 0:
            return False

        for d in [2, 3, 5]:
            while num % d == 0:
                num /= d
        return num == 1

s = Solution()
print(s.isUgly(1))
print(s.isUgly(2))
print(s.isUgly(3))
print(4, s.isUgly(4))
print(5, s.isUgly(5))
print(s.isUgly(6))
print(s.isUgly(14))