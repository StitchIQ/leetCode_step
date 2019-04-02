#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 11:51

# @File    : leetCode_171.py

'''
excel 字母转数字
思路：从末尾字母开始转，最后位的字母为实际数字，次位字母乘以26的位次方，以此类推
组后相加，得到数字

思路2：
结果初始值为0， 从高位开始转，直接转的结果赋值。
此值在下一轮循环中乘以26，以此类推。
算法本质是 123 =
1
1×10 + 2
（1×10+2）×10 + 3
'''


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2 = s[::-1]
        temp = 0
        for i, k in enumerate(s2):
            temp += (ord(k) - 64)*26**i

        return temp

        # ans = 0
        # for e in s:
        #     ans = ans * 26 + ord(e) - ord("A") + 1
        #
        # return ans

s = Solution()
print(s.titleToNumber("A"))
print(s.titleToNumber("B"))
print(s.titleToNumber("Z"))
print(s.titleToNumber("AA"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("ZY"))
print(s.titleToNumber("AAA"))

