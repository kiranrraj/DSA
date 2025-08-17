# Date: 15/08/2025
# Question: 5 
# Level: Easy
# Code: Python
# Question: You are given an integer array nums and an integer val. Your task is to remove all 
#           occurrences of val from nums in-place. After removing all occurrences of val, return 
#           the number of remaining elements, say k, such that the first k elements of nums do 
#           not contain val. The order of the elements which are not equal to val does not matter. 
#           It is not necessary to consider elements beyond the first k positions of the array. 
#           To be accepted, the first k elements of nums must contain only elements not equal to val. 
#           Return k as the final result.


def removeElement(nums: list[int], val: int) -> int:
    tmp = []
    for num in nums:
        if num == val:
            continue
        tmp.append(num)
    # to return the same array, rather than a new array    
    for i in range(len(tmp)):
        nums[i] = tmp[i]
    return len(tmp)

nums = [1, 2, 3, 4, 4, 4, 5, 6]
val = 4

print(removeElement(nums, val))

# Time complexity O(n)
# Space complexity O(n)