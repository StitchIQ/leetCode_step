#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 14:39
# @File    : leetCode_541.py

'''
思路：
从0开始，步长为 2k,
取前k个字段反转，后k个字段保持

'''


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        for i in range(0, len(s), 2*k):
            res += s[i:i + k][::-1]
            res += s[i + k: i + 2*k]
        return res

ss = "abcdefg"

s = Solution()
print(s.reverseStr(ss, 2))