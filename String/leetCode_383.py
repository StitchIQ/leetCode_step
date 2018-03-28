#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 19:59
# @File    : leetCode_383.py

'''
判断是否包含
思路，使用set
'''


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for r in ransomNote:
            if r not in d:
                if ransomNote.count(r) > magazine.count(r):
                    return False
                else:
                    d[r] = 1
        return True

s = Solution()
r = s.canConstruct("aa", "aab")
print(r)