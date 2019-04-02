#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 10:52

# @File    : leetCode_69.py

'''
计算开方，只去整数

思路：
一个数的开方不会大于n/2,
使用牛顿法
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x//2
        while 1:
            if n * n <= x < (n + 1)*(n + 1):
                return n
            n = int((n + x/n)/2)
            print(n)

        # t = x
        # while t * t > x:
        #     t = int(t / 2.0 + x / (2.0 * t))
        # return t
        import math
        return int(math.sqrt(x))


s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(5))
print(s.mySqrt(2147395599))
