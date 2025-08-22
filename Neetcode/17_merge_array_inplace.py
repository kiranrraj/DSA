# Date: 22/08/2025
# Question: 17
# Level: Easy
# Code: Python
# Question: Merge Sorted Array

def merge(nums1, m, nums2, n):
    # three pointers
    # to end of the array nums1
    p_merged = m + n - 1
    # to end of valid element
    p1 = m - 1
    # to end of nums2
    p2 = n - 1

    while p2 >= 0:
        if p1>=0 and nums1[p1] >= nums2[p2]:
            nums1[p_merged] = nums1[p1]:
            p1 -= 1
        else:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
        p_merged -= 1


# Time complexity: O(n)
# Space complexity: O(1)

# p1: Points to the last valid element of nums1 (at index m - 1).
# p2: Points to the last element of nums2 (at index n - 1).
# p_merged: Points to the last available position in nums1 
# where the merged elements will be placed (at index m + n - 1).

# The algorithm loops backward from the end of both arrays. 
# At each step, it compares the elements at nums1[p1] and 
# nums2[p2].

# If nums1[p1] is greater than or equal to nums2[p2], means
# nums1[p1] is the largest and it is placed at nums1[p_merged] 
# then p1 and p_merged is decremented.

# If nums2[p2] is larger, it's placed at nums1[p_merged], and 
# p2 and p_merged decremented.

# The loop continues as long as p2 is valid. 
# The remaining elements in nums1 are already in their correct 
# places at the beginning of the array, so no more comparisons 
# needed.