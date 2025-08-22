# Date: 22/08/2025
# Question: 15
# Level: Easy
# Code: Python
# Question: Merge Strings Alternately


def mergeAlternately(word1, word2):
    minLength = min(len(word1),len(word2))
    temp = []

    for i in range(minLength): 
        temp.append(word1[i])
        temp.append(word2[i])

    if word1[minLength:]:
        temp.extend(word1[minLength:])
    elif word2[minLength:]:
        temp.extend(word2[minLength:])
    
    return "".join(temp)


s = "Hello"
t = "World"
print(f"{s} + {t} alternately = {mergeAlternately(s, t)}")

# Time complexity: O(m+n) 
# Space complexity: O(m+n) 