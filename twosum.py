#1: Two Sum
# Given an array of integers num and an integer target, return indices of the two numbers such that they add up to
# target

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i, num in enumerate(nums):
            j = target - num
            if j in dict:
                return [dict[j], i]
            else:
                dict[num] = i
