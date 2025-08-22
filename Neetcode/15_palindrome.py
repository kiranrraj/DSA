# Date: 22/08/2025
# Question: 15
# Level: Easy
# Code: Python
# Question: Valid Palindrome

import re

def isPalindromeRegex(s: str) -> bool:
    pattern = r'[a-zA-Z0-9]'
    cleanedText = cleanedText = "".join(re.findall(pattern, s.lower()))
    length = len(cleanedText)
    
    for i in range(length//2):
        if cleanedText[i] != cleanedText[length-1-i]:
            return False
    return True

def isPalindrome(s):
    cleaned_s = ""
    for char in s:
        if char.isalnum():
            cleaned_s+= char.lower()

    return cleaned_s == cleaned_s[::-1]

s = "Malayalam"
s1 = "Kiran"

print(f"Is '{s}' Palindrome: {isPalindromeRegex(s)}")
print(f"Is '{s1}' Palindrome: {isPalindrome(s1)}")

# For both functions
# The check for alphanumeric, lower function take O(n) time and space
# Time complexity:  O(n)
# Space complexity: O(n)