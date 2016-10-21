"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Coding by Xiaohui
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        my idea is to enumerate every element in nums and check whether can find (target - it) in nums
        """
        answer = {}
        i = 0
        for i, e in enumerate(nums):
            if target - e in answer:
                return [answer[target - e], i]
            answer[e] = i

if __name__ == '__main__':
    print Solution().twoSum((3, 4, 6, 7, 11, 15), 9)