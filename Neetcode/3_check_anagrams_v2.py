# Date: 13/08/2025
# Question: 3 (Version 2)
# Level: Easy
# Code: Python
# Question: Given two strings s and t, return true if the two strings are anagrams of each other, 
#           otherwise return false. An anagram is a string that contains the exact same characters 
#           as another string, but the order of the characters can be different.

## Hash Table (Using Array)
def isAnagram(s, t) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True

word1 = "kiran"
word2 = "irank"

print(isAnagram(word1, word2)) # True

word3 = "irank0"
print(isAnagram(word3, word2)) # False

# Time Complexity: O(n + m) 
# Space Complexity: O(k) [Number of unique characters in the string]