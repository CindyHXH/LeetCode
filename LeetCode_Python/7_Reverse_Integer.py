"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Coding by Xiaohui
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        set return value as result
        use flag to distinct negative integer
        """

        result = 0
        flag = 0
        if x < 0:
            flag = 1
            x = -x
        while x > 0:
            result = result * 10 + x % 10
            x /= 10

        if flag == 1:
            result = -result
        """
        Handle Overflow
        """
        if result < -(1 << 31) or result > (1 << 31) - 1:
            result = 0

        return result

if __name__ == "__main__":
    print Solution().reverse(123)
    print Solution().reverse(-321)