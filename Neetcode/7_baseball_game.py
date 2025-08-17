# Date: 17/08/2025
# Question: 7
# Level: Easy
# Code: Python
# Question: You are keeping the scores for a baseball game with strange rules. At the 
#           beginning of the game, you start with an empty record. Given a list of strings 
#           operations, where operations[i] is the ith operation you must apply to the 
#           record and is one of the following:
#               An integer x: Record a new score of x.
#               '+': Record a new score that is the sum of the previous two scores.
#               'D': Record a new score that is the double of the previous score.
#               'C': Invalidate the previous score, removing it from the record.
#               Return the sum of all the scores on the record after applying all the operations.

def calPoints(operations):
    result = []
    out = 0
    for i in operations:
        if i.lstrip("+-").isdigit():
            result.append(int(i))
        elif i == "+":
            if len(result) >= 2:
                result.append(result[-1] + result[-2])
        elif i == "D":
            if len(result) >= 1:
                result.append(result[-1] *2)
        elif i == "C":
            if len(result) >= 1:
                result.pop()
    for i in result:
        out+=i
    return out     

# Time Complexity: O(n)
# Space Complexity: O(n)

# Better answer
# stack = []
# for op in operations:
#     if op == "+":
#         stack.append(stack[-1] + stack[-2])
#     elif op == "D":
#         stack.append(2 * stack[-1])
#     elif op == "C":
#         stack.pop()
#     else:
#         stack.append(int(op))
# return sum(stack)