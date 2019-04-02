#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 18:37

# @File    : leetCode_441.py
'''
思路，问题的本质是 n是否为等差数列的和
等差数列k*(+1) = 2n
使用2n开方，然后判断开方值是大于2n，来决定是否加 -1
'''

from math import sqrt

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n <= 2:
            return 1
        n2 = n * 2
        res = int(sqrt(n2))
        s_sum = res * (res + 1)
        print(res)
        if s_sum <= n2:
            return res
        elif s_sum > n2:
            return res - 1

        # 优秀答案
        # return int(math.sqrt(2 * n + 0.25) - 0.5)

s = Solution()
s.arrangeCoins(0)
s.arrangeCoins(1)
s.arrangeCoins(2)
s.arrangeCoins(3)
s.arrangeCoins(1804289383)

