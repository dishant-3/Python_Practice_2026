# def binarySubstring(s):
#     n = len(s)
#     substr=[]
#     res_count =0
#     for i in range(n):
#         for j in range(i+1,n):
#             substr.append(s[i:j]) 
        
#     for ele in substr:
#         print(f"Substring is:\n{ele}")
#         if ele[0]==ele[-1] and ele[0]== '1':
#             res_count+=1
#         print(f"Result count:{res_count}")

#     return res_count

## Approach 2: Naive approach without storing the substrings and checking directly start and end index elements
# def binarySubstring(s):
#     n = len(s)
#     count =0

#     for i in range(n):
#         if s[i] == '1':
#             for j in range(i+1,n):
#                 if s[j] == '1':
#                     count += 1
#     return count

## Approach 3: Using mC2 cobinations of 1 out of m 

def binarySubstring(s):
    n =len(s)
    ones_cnt = 0
    for i in range(n):
        if s[i] == '1':
            ones_cnt += 1
    res = ones_cnt *(ones_cnt-1) //2
    return res


s1 = "00100101"
print(f"Input:{s1}\n result:{binarySubstring(s1)}")  

s2 = "1111"
print(f"Input:{s2}\n result:{binarySubstring(s2)}") 

        
