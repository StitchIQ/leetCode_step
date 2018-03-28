#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 16:52
# @File    : leetCode_20.py

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 1:
            return True
        if len(s) == 1:
            return False

        stack = []

        for sub in s:
            if sub in ("(", "[", "{"):
                stack.append(sub)
            elif len(stack) == 0:
                return False
            if sub in (")", "]", "}") and stack:
                if sub == ")" and stack[-1] == "(":
                    stack.pop()
                    continue
                elif sub == "]" and stack[-1] == "[":
                    stack.pop()
                    continue
                elif sub == "}" and stack[-1] == "{":
                    stack.pop()
                    continue
                else:
                    stack.append(sub)
                    break

            if sub in (")", "]", "}") and len(stack) == 0:
                stack.append(sub)
                break

        # print(stack)
             #   参考代码
                # sample = {
                #     "}": "{",
                #     "]": "[",
                #     ")": "("
                # }
                # for sub in s:
                #     if sub in ("(", "[", "{"):
                #         stack.append(sub)
                #     else:
                #         if len(stack) == 0:
                #             return False
                #         temp = stack.pop()
                #         if sample[sub] == temp:
                #             continue
                #         else:
                #             return False
        return len(stack) == 0

import time
start = time.time()
s = Solution()
assert s.isValid("") == True
assert s.isValid("((())){{{}}}[[[]]]") == True
assert s.isValid("()[]{}") == True
assert s.isValid("()") == True
assert s.isValid("(]") == False
assert s.isValid("([)]") == False
assert s.isValid("([)]") == False
assert s.isValid("]]][[[") == False
assert s.isValid("(])") == False
assert s.isValid("[])") == False
print(time.time() - start)
