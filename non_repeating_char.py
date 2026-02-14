## Approach 1: Using hashmap to calculate count of elements
def nonRepeatingChar(s):
    # n = len(s)
    counter_dict ={}
    for ele in s:
        counter_dict[ele]= counter_dict.get(ele,0)+1
    # print(f"Dictionary of counts: {counter_dict}")    
    for ele in s:
        if counter_dict[ele] == 1:
            return ele
    return '$'

s = "geeksforgeeks"
res = nonRepeatingChar(s)
print(f"Input: {s}\n Output:{res}")

## approach 2: Using collections library
# from collections import Counter

# def nonRepeatingChar(s):
#     counter_dict = Counter(s)   # Automatically counts each character
#     print(f"Dictionary of counts: {counter_dict}")

#     for ele in s:
#         if counter_dict[ele] == 1:
#             return ele
#     return '$'

# s = "geeksforgeeks"
# res = nonRepeatingChar(s)
# print(f"Input: {s}\nOutput: {res}")

## Brute Force approach : Traversing the string using two loops

def nonRepeatingEle(s):
    n =len(s)
    for i in range(n):
        found = False
        for j in range(n):
            if i!=j and s[i] == s[j]:
                found = True
                break
        if not found:
            return s[i]
    return '$'
str1 ="racecar"
res1 = nonRepeatingEle(str1)
print(f"Input:{str1}\n Output:{res1}")
str2 = "rdmardma"
res2 = nonRepeatingEle(str2)
print(f"Input:{str2}\n Output:{res2}")

## Most optimised solution

def nonRep(s):
    MAX_CHAR = 26
    vis = [-1] * MAX_CHAR

    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        if vis[index] == -1:
            
            # Store the index when character is first seen
            vis[index] = i  
        else:
            
            # Mark character as repeated
            vis[index] = -2  

    idx = -1

    # Find the smallest index of the non-repeating characters
    for i in range(MAX_CHAR):
        if vis[i] >= 0 and (idx == -1 or vis[i] < vis[idx]):
            idx = i

    return '$' if idx == -1 else s[vis[idx]]


s = "aabbccc"
print(nonRep(s))
