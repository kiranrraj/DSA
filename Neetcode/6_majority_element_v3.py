# Date: 16/08/2025
# Question: 6
# Level: Easy
# Code: Python
# Question: Given an array nums of size n, return the majority element. The majority element is the element 
# that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

# Since the majority element appears more than half the time, it will occupy more than half of the array's indices. 
# This means that no matter how the other elements are arranged, the majority element's block will be long enough to 
# cover the middle index of the array,

# Sorting method
def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]

nums1 = [4,4,4,2,3,3,3,4,4,4,4,4,4,3,3,3]
print("Majority element in the array is :",majorityElement(nums1))

# Time Complexity: O(n logn)
# Space Complexity: O(1) or O(n), depends on sorting algorithm.