# Date: 13/08/2025
# Question: 2 version1
# Level: Easy
# Code: Python
# Question: Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

from typing import List

def hasDuplicate(nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

nums1 = [1,2,3,4,5,6,7]
print(hasDuplicate(nums1))  # False

nums2 = [1,2,3,1,7,8]
print(hasDuplicate(nums2)) # True


# Time Complexity: O(n^2)
# Space Complexity: O(1)
