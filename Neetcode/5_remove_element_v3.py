# Date: 15/08/2025
# Question: 5 
# Level: Easy
# Code: Python
# Question: You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.
#           After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of 
# nums do not contain val. The order of the elements which are not equal to val does not matter. It is not necessary to consider 
# elements beyond the first k positions of the array. To be accepted, the first k elements of nums must contain only elements 
# not equal to val. Return k as the final result.

# Two pointer
def removeElement(self, nums: list[int], val: int) -> int:
    # k is a write pointer, it tracks the position where the next element which is not equal to val should be placed.
    k = 0
    # i is the read pointer, it loop through index in nums.
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [1, 2, 3, 4, 4, 4, 5, 6]
val = 4

print(removeElement(nums, val))

# Time complexity O(n)
# Space complexity O(1)