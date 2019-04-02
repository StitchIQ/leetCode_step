#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 10:59

# @File    : leetCode_415.py
'''
解题思路，
先把两个字符串倒序，按照每一位进行相加，然后进位

优秀答案：把字符串填充为长度一样的，然后处理
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s1_len = len(num1)
        s2_len = len(num2)
        min_len = min(s1_len, s2_len)
        total = []
        s1 = [int(i) for i in num1][::-1]
        s2 = [int(i) for i in num2][::-1]
        if s1_len >= s2_len:
            s3 = s1[min_len:]
        else:
            s3 = s2[min_len:]
        t2 = 0
        for i in range(min_len):
            temp = s1[i] + s2[i] + t2
            if temp < 10:
                total.append(temp)
                t2 = 0
            else:
                total.append(temp % 10)
                t2 = 1

        for i in range(len(s3)):
            if s3[i] + t2 < 10:
                total.append(s3[i] + t2)
                t2 = 0
            else:
                total.append((s3[i] + t2) % 10)
                t2 = 1

        if t2:
            total.append(t2)

        print(total[::-1])
        print("".join([str(t) for t in total[::-1]]))

s = Solution()
s.addStrings("111", "222")
s.addStrings("1", "999")