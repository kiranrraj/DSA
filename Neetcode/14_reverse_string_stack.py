# Date: 21/08/2025
# Question: 14
# Level: Easy
# Code: Python
# Question: Reverse a string using stack

def reverseString(s):
    temp = []
    for char in s:
        temp.append(char)

    i =0
    while temp:
        s[i] = temp.pop()


s = list("kiran raj")
print(f"String: {s}")
reverseString(s)
print(f"Reversed String: {s}")

# Time complexity: O(n)
# Space complexity: O(n)