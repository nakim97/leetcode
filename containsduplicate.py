# 217: Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lst = {}
        for i in nums:
            if i in lst:
                return True
            else:
                lst[i] = 1
        return False