#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 11:07

# @File    : leetCode_728.py

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right + 1):
            temp = str(i)
            for j, t in enumerate(temp):
                if '0' in temp or i % int(t) != 0:
                    break
                if j + 1 == len(temp):
                    res.append(i)

        return res

s = Solution()
s.selfDividingNumbers(1, 22)

print(15 % 5)