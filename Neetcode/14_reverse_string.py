# Date: 21/08/2025
# Question: 14
# Level: Easy
# Code: Python
# Question: Reverse a string

def reverseString(s):
    length = len(s)
    for i in range(length//2):
        s[i], s[length-1-i] = s[length-1-i], s[i]

s = list("kiran")
print(f"String: {s}")
reverseString(s)
print(f"Reversed String: {s}")

# Time complexity: O(n)
# Space complexity: O(1)

# Same result, with same time and space complexity 
# def reverseString(self, s: List[str]) -> None:
#     l, r = 0, len(s) - 1
#     while l < r:
#         s[l], s[r] = s[r], s[l]
#         l += 1
#         r -= 1