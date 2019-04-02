#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/27 17:06

# @File    : leetCode_168.py

'''
思路：
对n进行26 整除，所的数用模26后转成字母。
n = （n-1）// 26，直到n<0。

对所得字符串反转，得到结果。
小技巧，字符转时，使用（n-1）模26，然后用


1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB
'''


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 思路问题，没有深入理解进制的特点，造成判断混乱
        b = n % 26 if n % 26 != 0 else 26
        res = chr(b + 64)
        temp = n
        while temp > 0:
            temp = temp // 26
            a = temp % 26 if temp % 26 != 0 else 26
            res += chr(64 + a)
        return res[::-1]

    def s2(self, n):

        s = ""
        while n > 0:
            s += chr(ord("A") + (n-1) % 26)
            n = (n-1) // 26

        return s[::-1]

# print(chr(26//26+64)+chr(26 % 27 + 64))
# print(26*26//26)
s = Solution()
print(s.s2(26*26*26 + 5))
print(100, s.s2(100))
print(1, s.s2(1))
print(26, s.s2(26))
print(27, s.s2(27))
print(28, s.s2(28))
print(52, s.s2(52))
print(53, s.s2(53))
print(701, s.s2(701))  # ZY
print(703, s.s2(703))  # ZY
print(26//26)
