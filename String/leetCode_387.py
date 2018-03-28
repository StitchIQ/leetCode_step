#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 11:10
# @File    : leetCode_387.py


'''
题目分析：
找到字符串中第一个唯一的字母

思路
用count类，然后遍历字符串，遇到第一个为1的字母即返回
遍历结束还没有，则返回-1

'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        mydict = collections.Counter(s)
        for i, v in enumerate(s):
            if mydict[v] == 1:
                return i
        return -1

s = Solution()
print(s.firstUniqChar("loveleetcode"))