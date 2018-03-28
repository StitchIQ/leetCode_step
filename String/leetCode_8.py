#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 15:55
# @File    : leetCode_8.py


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        temp = str.strip()
        if not temp:
            return 0
        res = []
        pa = []
        for t in temp:
            if t in ("+", "-"):
                pa.append(t)
                if len(pa) > 1:
                    return 0
                continue
            if t in "0123456789":
                res.append(t)
                continue
            else:
                break
        if len(res) < 1:
            return 0
        pa.append(pa[0] if len(pa) > 0 else "+")
        res = int(pa[0] + "".join(res))
        if res > 2147483647:
            res = 2147483647
        if res < -2147483648:
            res = -2147483648

        return res

s = Solution()
print(s.myAtoi("-1"))
print("  +-12  ".index("-"))
