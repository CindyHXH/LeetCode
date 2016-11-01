"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Coding by Xiaohui
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        If right Roman is large than left Roman, then right minus left (only applys for I, X, C)
        IF right Roman is no more than left Roman, then right plus left
        """

        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in xrange(len(s)):
            if i + 1 < len(s) and ROMAN[s[i]] < ROMAN[s[i+1]]:
                result -= ROMAN[s[i]]
            else:
                result += ROMAN[s[i]]

        return result

if __name__ == "__main__":
    print Solution().romanToInt("XXIX")
    print Solution().romanToInt("CDXV")
    print Solution().romanToInt("MMMCMXCIIII")




