# Date: 13/08/2025
# Question: 3 (Version 1)
# Level: Easy
# Code: Python
# Question: Given two strings s and t, return true if the two strings are anagrams of each other, 
#           otherwise return false. An anagram is a string that contains the exact same characters 
#           as another string, but the order of the characters can be different.


def getCount(msg):
    letter_dict = {}
    for i in msg:
        letter_dict[i] = letter_dict.get(i,0) + 1 
    return letter_dict
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    sCount = getCount(s)
    tCount = getCount(t)
    return sCount == tCount

word1 = "kiran"
word2 = "irank"

print(isAnagram(word1, word2)) # True

word3 = "irank0"
print(isAnagram(word3, word2)) # False

# Time Complexity: O(n + m) 
# Space Complexity: O(k) [Number of unique characters in the string]
