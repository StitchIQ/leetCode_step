#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 19:10
# @File    : leetCode_521.py

'''
如果a，b长度不同，则返回长度较长的
如果长度相同，相等则返回-1

python bool和值进行逻辑运算，结果为 后面的变量值
'''

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # return (a != b and max(len(a), len(b))) or -1
        return (max(len(a), len(b)) and a != b) or -1


s = Solution()
print(s.findLUSlength("aba", "cbc"))
print( True and 3)
print( 3 and True)