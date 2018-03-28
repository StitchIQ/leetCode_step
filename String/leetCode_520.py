#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 17:27
# @File    : leetCode_520.py


'''
判断大写字母是否使用正确
1、全部大写
2、首字母大写
3、全小写字母

'''


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper():
            return True

        if word == word.lower():
            return True

        if word[0].isupper() and word[1:] == word[1:].lower():
            return True
        return False

        # return word.isupper() or word.islower() or word.istitle()

ss = "Google"
print(ss[1:])