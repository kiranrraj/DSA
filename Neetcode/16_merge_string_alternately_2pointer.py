# Date: 22/08/2025
# Question: 16
# Level: Easy
# Code: Python
# Question: Merge Strings Alternately


def mergeAlternately(word1, word2):
    n = len(word1)
    m = len(word2)
    i = j = 0
    temp = []

    while i < n or j < m:
        if i < n:
            temp.append(word1[i])
        if j < m:
            temp.append(word2[j])
        i += 1
        j += 1
    
    return "".join(temp)


s = "Hello"
t = "World"
print(f"{s} + {t} alternately = {mergeAlternately(s, t)}")

# Time complexity: O(m+n) 
# Space complexity: O(m+n) 