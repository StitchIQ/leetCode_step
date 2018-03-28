#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 16:55
# @File    : leetCode_557.py


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #ss = s.split(" ")
        return " ".join([t[::-1] for t in s.split(" ")])
        # return ' '.join(s.split()[::-1])[::-1]

ss = "Let's take LeetCode contest"
s = Solution()
dd = s.reverseWords(ss)
print(ss)
print(dd)