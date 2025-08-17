# Date: 14/08/2025
# Question: 4
# Level: Easy
# Code: Python
# Question: You are given an array of strings strs. Return the longest common prefix of all the strings. 
#           If there is no longest common prefix, return an empty string "".


## Vertical Scanning
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) <1:
        return ""

    if len(strs) ==1:
        return strs[0]

    reference_word = strs[0]
    for i in range(len(reference_word)):
        char_to_check = reference_word[i]
        for word in strs[1:]:
            if i >= len(word) or word[i] != reference_word[i]:
                return reference_word[:i]
    return reference_word

words1 =["basket", "ball", "bottle"]
print(longestCommonPrefix(words1))

words2 = ["Plastic", "Plate"]
print(longestCommonPrefix(words2))

# Time complexity: O(n*m)
# Space Complexity: O(1)
