# Date: 15/08/2025
# Question: 5 
# Level: Easy
# Code: Python
# Question: You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.
#           After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of 
# nums do not contain val. The order of the elements which are not equal to val does not matter. It is not necessary to consider 
# elements beyond the first k positions of the array. To be accepted, the first k elements of nums must contain only elements 
# not equal to val. Return k as the final result.

from typing import List
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            i-=1
        i+=1
    return len(nums)

nums = [1, 1, 3, 4, 5, 6]
val = 1
print(removeElement(nums, val))


# | Case       | Time Complexity | Space Complexity |
# | ---------- | --------------- | ---------------- |
# | Best Case  | O(n)            | O(1)             |
# | Worst Case | O(n²)           | O(1)             |
