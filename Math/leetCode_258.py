#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 17:08

# @File    : leetCode_258.py
'''
1、思路，数直接模10，然后相加
最后小于10 时停止，使用递归的方法

2、 不使用循环

'''


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        s = 0
        while num > 0:
            s += num % 10
            num = num // 10

        return self.addDigits(s)

        # if not num:
        #     return 0
        # return (num - 1) % 9 + 1

s = Solution()

print(s.addDigits(32))
print(s.addDigits(100))
print(s.addDigits(144))

print(bin(38))