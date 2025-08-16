# Date: 16/08/2025
# Question: 6
# Level: Easy
# Code: Python
# Question: Given an array nums of size n, return the majority element. The majority element is the element 
# that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

# The Boyer-Moore Voting Algorithm finds the majority element by leveraging the fact that the majority element's 
# frequency is greater than the combined frequency of all other elements. The algorithm works by pairing each 
# occurrence of a non-majority element with a single occurrence of the majority element, effectively cancelling 
# them out. Since the majority element appears more than half the time, it will be the last one standing with a positive count.

def findMajorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count+=1
        else:
            count-=1
    return candidate

nums1 = [4,4,4,2,3,3,3,4,4,4,4,4,4,3,3,3]
print(findMajorityElement(nums1))

# Time Complexity: O(n)
# Space Complexity: O(1)