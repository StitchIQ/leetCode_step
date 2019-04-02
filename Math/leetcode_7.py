__author__ = 'stitch'


'''
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
click to show spoilers.
Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = int(str(abs(x))[::-1])
        if x > 0:
            y = s
        else:
            y = -1 * s
        if -2147483648 > s or 2147483647 < s:
            y = 0

        return y


print(Solution().reverse(123))
