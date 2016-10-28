"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

Coding by Xiaohui
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        Distance between 2 zigzag is 2*numRows - 2
        Distance between middle element and its start line is 2*(numRows - 1 - i)
        """
        if numRows == 1:
            return s
        step = 2 * numRows - 2
        result = ""
        for i in xrange(numRows):
            for j in xrange(i, len(s), step):
                result += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    result += s[j + step - 2 * i]
        return result


if __name__ == "__main__":
    print Solution().convert("TOMORROWISANOTHERDAY", 3)
    print Solution().convert("TOMORROWISANOTHERDAY", 4)
    print Solution().convert("TOMORROWISANOTHERDAY", 5)


