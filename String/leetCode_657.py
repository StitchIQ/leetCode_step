#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 16:45
# @File    : leetCode_657.py

'''
思路，
U,D,L,R
分布对应+1， -1操作，最后比较值即可
'''


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        steps = {
            "U": 1,
            "D": -1,
            "L": -1,
            "R": 1
        }
        a, b = 0
        for m in moves:
            if m in ("U", "D"):
                a += steps[m]
            if m in ("L", "R"):
                b += steps[m]
        return a == 0 and b == 0

        # 充分利用str的库的方法，经典
        # return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')