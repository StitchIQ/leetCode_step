
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x = str(x)
        temp = x[::-1]
        return temp == x


s = Solution()

print(s.isPalindrome(1001))

