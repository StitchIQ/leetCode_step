#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 15:54
# @File    : leetCode_686.py

'''
思路：
使用正则表达式  超时

参考答案
times = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a))
for i in range(2):
  if B in (A * (times + i)):
    return times + i
return -1
'''


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        import re

        i = 1
        p2 = re.compile(B)
        while True:
            if p2.search(A*i):
                return i
            i += 1
            if len(A) > len(B) * 5:
                break

        pat = re.compile(A)
        if not pat.search(B):
            return -1

        return -1


s1 = "abcd"
s2 = "cdabcdab"
s = Solution()
# s.repeatedStringMatch(s1, s2)
print(s.repeatedStringMatch("aaaa", "a"))