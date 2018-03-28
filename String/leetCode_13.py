#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 14:32
# @File    : leetCode_13.py

'''
罗马数字转换为int
思路：从头向后转，定义一个转换字典
如果新的数比 已经转换的最后一个数大，则已经转换的最后一个数设置为负，
最后求和

'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Ⅰ（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）
        res = []
        for k in s:
            if res and roma[k] > res[-1]:
                res[-1] = - res[-1]
            res.append(roma[k])
        print(res)
        # for i in res[::-1]:

        return sum(res)


s = Solution()

print(s.romanToInt("MCMLXXX")) # 1980    MMMCMXCIX 3999
print(s.romanToInt("MMMCMXCIX"))