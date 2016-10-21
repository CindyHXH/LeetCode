"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Coding by Xiaohui
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(reversed(s))

if __name__ == "__main__":
    print Solution().reverseString("hello")
    print Solution().reverseString("yoho")