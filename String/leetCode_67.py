#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/27 10:39
# @File    : leetCode_67.py

'''
思路，按照每位相加，考虑进位，以及长度较长的字符串

最有思路
a = int(a, 2)
        b = int(b, 2)
        return ("" + bin(a+b))[2:]
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        res = ["0"]*(max(len_a, len_b))
        carry = 0
        for i in range(-1, -min(len_a, len_b)-1, -1):
            a_i = int(a[i])
            b_i = int(b[i])
            if a_i + b_i + carry > 2:
                res[i] = "1"
                carry = 1
                continue
            if a_i + b_i + carry == 2:
                res[i] = "0"
                carry = 1
                continue
            if a_i + b_i + carry == 1:
                res[i] = "1"
                carry = 0
                continue
            if a_i + b_i + carry == 0:
                res[i] = "0"
                carry = 0
                continue
            # print(res)
        temp = a if len_a >= len_b else b
        for i in range(-min(len_a, len_b)-1, -len(res)-1, -1):
            if int(temp[i]) + carry == 2:
                res[i] = "0"
                carry = 1
            else:
                res[i] = str(int(temp[i]) + carry)
                carry = 0
                # break
        if carry:
            res.insert(0, '1')
        return "".join(res)

s = Solution()
# print(s.addBinary("11", "10"))
# print(s.addBinary("11", "11"))
print(s.addBinary("1", "1"))
print(s.addBinary("1011", "1010"))

def ss(a, b):
    a = int(a, 2)
    b = int(b, 2)
    print(bin(a+b))
    return ("" + bin(a + b))[2:]

print(ss("1011", "1010"))