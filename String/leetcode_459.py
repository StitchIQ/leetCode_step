#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 12:10
# @File    : leetCode_459.py


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for i in range(len(s)):
            tmp = s[i: i+2]
            for j in range(1, len(tmp)-1):
                if s[j:2] == tmp:
                    return True

        return False

        # size = len(s)
        # next = [0] * size
        # for i in range(1, size):
        #     k = next[i - 1]
        #     while s[i] != s[k] and k:
        #         k = next[k - 1]
        #     if s[i] == s[k]:
        #         next[i] = k + 1
        # p = next[-1]
        # return p > 0 and size % (size - p) == 0

print(Solution().repeatedSubstringPattern("bb"))

print(Solution().repeatedSubstringPattern("aba"))