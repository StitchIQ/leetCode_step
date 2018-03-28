#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 14:21
# @File    : leetCode_125.py

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = s.lower()
        # temp = s[::-1]
        # print(s)
        # print(temp)
        # i = len(s) - 1
        # j = i
        # p = True
        # while p and i > 0:
        #     # print("i ,j :", i, j)
        #     a = ord(s[i])
        #     b = ord(temp[j])
        #     # print("a b :", a, b)
        #     if 97 <= a <= 122 or 48 <= a <= 57:
        #         if 97 <= b <= 122 or 48 <= b <= 57:
        #             print("res : ", a^b, s[i], temp[j])
        #             p = a^b == 0
        #             i -= 1
        #             j -= 1
        #         else:
        #             j -= 1
        #     else:
        #         i -= 1
        # return p

        temp = [i.lower() for i in s if i.isalnum()]
        return temp == temp[::-1]

s = Solution()
print("P ", s.isPalindrome("A man, a plan, a canal: Panama"))
print("P ", s.isPalindrome("race a car"))
