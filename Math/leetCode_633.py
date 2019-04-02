#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 11:41

# @File    : leetCode_633.py

'''
给定一个数，判断段是否是两个数的平方和
即是否满足n = a * a + b* b

思路：
从n/2 开始，判断n - x*x 是否也为平方数，

int(num**0.5)==num**0.5
'''


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        for i in range(0, int(c**0.5)+1):
            s = i * i
            if self.isquare(c - s):
                return True
        return False

    def isquare(self, n):
        return int(n**0.5) == n**0.5

s = Solution()
print(s.judgeSquareSum(2))
print(s.judgeSquareSum(4))
print(s.judgeSquareSum(5))
print(s.judgeSquareSum(25))
