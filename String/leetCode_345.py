#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 15:13
# @File    : leetCode_345.py

'''
反转元音字母
思路：
先找出元音字母，并记录位置
然后把位置最后的字母放到最前面的位置
'''


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        res = list(s)
        index = []
        vw = []
        for i in range(len(s)):
            if s[i] in vowels:
                index.append(i)
                vw.append(s[i])

        for i in range(len(index)):
            res[index[i]] = vw[len(index) - 1 - i]

        return "".join(res)

s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))  # leotcede
ss = "leetcode"
print(list(ss))

