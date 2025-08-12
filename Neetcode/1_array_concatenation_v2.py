# You are given an integer array nums of length n. 
# Create an array ans of length 2n where ans[i] == nums[i] 
# and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

from typing import List
def getConcatenation(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * 2 * n
    # print(result)

    for i, num in enumerate(nums):
        result[i] = result[n+i] = num
        # Above code is equivalent to 
        # ans[i] = num
        # ans[i + n] = num
    return result

numbers = [1,2,3,4,5]
print(getConcatenation(numbers))    
# Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]