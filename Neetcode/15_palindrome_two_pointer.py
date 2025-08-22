# Date: 22/08/2025
# Question: 15
# Level: Easy
# Code: Python
# Question: Valid Palindrome (Two Pointer)

def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        # Inside the loop, you have two nested while loops that 
        # handle non-alphanumeric characters. These loops advance 
        # the l and r pointers to the next valid character.
        while l < r and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        # If the characters match, you've successfully verified 
        # that this pair of characters is a palindrome. To check 
        # the next pair, you must move the pointers.
        l, r = l + 1, r - 1 
    return True

s = "Malayalam"
s1 = "Kiran"

print(f"Is '{s}' Palindrome: {isPalindrome(s)}")
print(f"Is '{s1}' Palindrome: {isPalindrome(s1)}")