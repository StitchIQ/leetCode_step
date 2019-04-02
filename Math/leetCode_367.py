#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 15:01

# @File    : leetCode_367.py


'''
计算一个数是否完全平方数
思路，
1、用牛顿放计算

2、数乘以0.5次方等于0。5次方取整
int(num**0.5)==num**0.5
'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = num

        while 1:
            print(n)
            if n * n == num:
                return True
            elif n * n < num:
                break
            n = int((n + num/n)/2)
        return False
s = Solution()
print(s.isPerfectSquare(16))
