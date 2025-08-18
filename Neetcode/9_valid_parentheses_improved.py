# Date: 18/08/2025
# Question: 9
# Level: Easy
# Code: Python
# Question: Valid Parentheses  

def isValidParentheses(s):
    pair = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    stack = []

    for char in s:
        # Check if it's an opening bracket
        if char in pair.values():  
            stack.append(char)
        # Check if it's a closing bracket
        elif char in pair.keys():  
            if not stack or stack.pop() != pair[char]:
                return False

    return len(stack) == 0

print(isValidParentheses("([{}])"))
print(isValidParentheses("[(])"))

# Time Complexity: O(n) 
# Space Complexity: O(n)