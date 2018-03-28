#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 15:31
# @File    : leetCode_12.py

'''
思路：
直接转换为str，然后按照位乘以 1000， 100，等

然后把这些分别转换为 罗马字母，然后 相加

参考思路：
从大到小列出罗马数字转折的关键点，
然后开始循环，如果大于则加罗马字母
然后数字减去关键数字，以此重复，直到结束
'''


class Solution(object):
    # def intToRoman(self, num):
    #     """
    #     :type num: int
    #     :rtype: str
    #     """
    #     res = []
    #     i = 1
    #     s = str(num)[::-1]
    #     for k in s:
    #         n = int(k) * i
    #         i *= 10
    #         if n <= 3:
    #             res.append("I"*n)
    #         if 3 < n <= 8:
    #             res.append("I"*(5-n) + "V" + "I"*(n-5))
    #         if 9 <= n <= 10:
    #             res.append("I"*(1 - n//10) + "X")
    #
    #         if 10 < n <= 30:
    #             res.append("X"*(int(n/10)))
    #
    #         if 30 < n <= 80:
    #             res.append("X"*(5 - int(n / 10)) + "L" + "X"*(int(n/10) - 5))
    #
    #         if 90 <= n <= 100:
    #             res.append("X" * (1 - int(n / 100)) + "C")
    #
    #         if 100 < n <= 300:
    #             res.append("C" * n // 100)
    #
    #         if 300 < n <= 800:
    #             res.append("C" * (5 - int(n / 100)) + "D" + "C"*(int(n/100) - 5))
    #
    #         if 900 <= n <= 1000:
    #             res.append("C" * (10 - int(n/100)) + "M")
    #         if 1000 < n < 4000:
    #             res.append("M" * int(n/1000))
    #
    #     return "".join(res[::-1])

    def int_to_roma(self, num):
        m = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        result = ""
        for n, s in m:
            while num >= n:
                result += s
                num -= n

        return result

    def intToRoman(self, num):
        arr = [(1000, "M"),
               (900, "CM"),
               (500, "D"),
               (400, "CD"),
               (100, "C"),
               (90, "XC"),
               (50, "L"),
               (40, "XL"),
               (10, "X"),
               (9, "IX"),
               (5, "V"),
               (4, "IV"),
               (1, "I")]
        res = ""
        for k, v in arr:
            while num >= k:
                res += v
                num -= k
        return res
s = Solution()
print(s.intToRoman(1980)) # MCMLXXX
print(s.intToRoman(3999)) # MMMCMXCIX
print(s.intToRoman(9))
print(s.intToRoman(10))
print(s.intToRoman(400))
print(s.intToRoman(101))
print(s.intToRoman(200))
