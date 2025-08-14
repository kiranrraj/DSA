# Date: 14/08/2025
# Question: 4 
# Level: Easy
# Code: Python
# Question: You are given an array of strings strs. Return the longest common prefix of all the strings. 
#           If there is no longest common prefix, return an empty string "".


## Horizontal Scanning
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    # The first string in the list is taken as the initial prefix.
    prefix = strs[0]
    # Start from the second string (i = 1) and compare it with the current prefix.
    for i in range(1, len(strs)):
        j = 0
        # ensures we don’t go out of bounds.
        while j < min(len(prefix), len(strs[i])):
            # If characters differ at any position, stop comparing.
            if prefix[j] != strs[i][j]:
                break
            j += 1
        # shorten prefix to the matching part only (from index 0 to j-1).
        prefix = prefix[:j]
    return prefix

words1 =["basket", "ball", "bottle"]
print(longestCommonPrefix(words1))

words2 = ["Plastic", "Plate"]
print(longestCommonPrefix(words2))

# Time complexity: O(n*m)
# Space Complexity: O(1)
