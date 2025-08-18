# Date: 18/08/2025
# Question: 9
# Level: Easy
# Code: Python
# Question: Valid Parentheses  

def isValidParentheses(s):
    input_list = list(s)
    opening = []
    pair = {
        "{" : "}",
        "[" : "]",
        "(" : ")"
    }
    
    for i in input_list:
        if i == "{" or i == "(" or i =="[":
            opening.append(i)
        else:
            if len(opening) > 0 and pair[opening[-1]] == i:
                opening.pop()
            else:
                return False
    if len(opening) != 0:
        return False
    return True

print(isValidParentheses("([{}])"))
print(isValidParentheses("[(])"))

# Time Complexity: O(n) 
# Space Complexity: O(n)