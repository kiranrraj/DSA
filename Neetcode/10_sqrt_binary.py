# Date: 19/08/2025
# Question: 10
# Level: Easy
# Code: Python
# Question: You are given a non-negative integer x, return the square root 
#           of x rounded down to the nearest integer. The returned integer 
#           should be non-negative as well. You must not use any built-in 
#           exponent function or operator.

# Binary search for the largest number whose square is still ≤ x
def mySqrt_binary(x: int) -> int:
    if x < 2:
        return x

    lo, hi = 1, x // 2
    ans = 1 

    while lo <= hi:
        mid = (lo + hi) // 2
        if mid <= x // mid:     # Equivalent to mid*mid ≤ x
            ans = mid 
            lo = mid + 1        # Try larger numbers
        else:
            hi = mid - 1

    return ans

print(mySqrt_binary(2))

# Binary Search Strategy
#   We keep a search range [lo, hi] of possible answers.
#   Pick mid = (lo+hi)//2.
#   Test: is mid*mid ≤ x?
#       Yes: mid is a candidate, but maybe there’s a bigger one.
#           Save it (ans = mid) and search to the right (lo = mid+1).
#       No: mid is too big, so shrink to the left (hi = mid-1).
# Repeat until the range is empty.