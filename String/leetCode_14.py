#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 15:26
# @File    : leetCode_14.py

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_len = len(strs)
        if str_len > 0:
            index_str = strs[0]
        else:
            return ""
        min_len = min(map(len, strs))
        index = -1
        loop = True
        for i in range(min_len):
            if not loop:
                break
            for j in range(str_len):
                if strs[j][i] != index_str[i]:
                    loop = False
                    break
                if j == str_len - 1:
                    index = i

        return index_str[:index+1] if index >= 0 else ""


tt = ["leet", "leet", "leetcode"]

s = Solution()
print(s.longestCommonPrefix(tt))
print(s.longestCommonPrefix(["a", "b"]))
print(s.longestCommonPrefix(["a"]))
print(s.longestCommonPrefix(["aca", "cba"]))
# print("sss ", min(map(len, tt)))
