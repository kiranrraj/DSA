# Date: 13/08/2025
# Question: 2 (version 2)
# Level: Easy
# Code: Python
# Question: Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

from typing import List

# Sorting method
def hasDuplicate(nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

nums1 = [1,2,3,4,5,6,7]
print(hasDuplicate(nums1))  # False

nums2 = [1,2,3,1,7,8]
print(hasDuplicate(nums2)) # True


# Time complexity: O(n logn)
# Space complexity: O(1) or O(n) based on sorting algorithm used.
