"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Coding by Xiaohui
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.strip().split()))



if __name__ == "__main__":
    print Solution().reverseWords("What a wonderful day")
    print Solution().reverseWords("time to sleep")