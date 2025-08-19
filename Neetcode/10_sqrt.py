# Date: 19/08/2025
# Question: 10
# Level: Easy
# Code: Python
# Question: You are given a non-negative integer x, return 
#           the square root of x rounded down to the nearest 
#           integer. The returned integer should be non-negative 
#           as well. You must not use any built-in exponent 
#           function or operator.
#
#
# Newton’s method: Guess, divide, average, repeat, stop when close enough.

# Heron’s Method
def findSqrt(x):
    if x < 2:
        return x
    x = r
    while r * r > x:
        r = (r + x // r) // 2
    return r

# Space complexity: O(1)
# Time complexity: O(log log x)

### Step by Step ###
# 1. Start with a guess.
#       Let’s say we want √10. Start with r = 10.
# 2. Divide x by your guess.
#       10 / 10 = 1.
#       If your guess is too big, x / r will be too small.
#       If your guess is too small, x / r will be too big.
# 3. Average your guess with x/r.
#       (r + x/r) / 2 pulls your guess closer to the real square root.
# 4. Repeat until it settles.

# Example: √10
# 1. Start r = 10
#       x/r = 10/10 = 1
#       Average = (10 + 1)/2 = 5.5
#       New guess = 5
# 2. Next r = 5
#       x/r = 10/5 = 2
#       Average = (5 + 2)/2 = 3.5
#       New guess = 3
# 3. Next r = 3
#       r * r = 9 which is just under 10
#       Stop ⇒ answer = 3 (floor of √10)