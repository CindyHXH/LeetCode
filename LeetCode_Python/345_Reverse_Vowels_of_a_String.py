"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # the idea is to check the position of vowels in string from left end and right end and switch them
        vowels = "aeiou"
        string = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if string[i].lower() not in vowels:
                i += 1
            elif string[j].lower() not in vowels:
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1

        return ''.join(string)


if __name__ == "__main__":
    print Solution().reverseVowels("happybirthday")
    print Solution().reverseVowels("enjoy")