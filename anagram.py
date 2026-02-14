## Approach 1 : Using counter for elements
# def areAnagrams(s1,s2):
#         dict_count1 = {}
#         dict_count2 = {}
    
#         for i in range(len(s1)):
#             if s1[i] in dict_count1:
#                 dict_count1[s1[i]] +=1
#             else:
#                 dict_count1[s1[i]] = 1
#         for i in range(len(s2)):
#             if s2[i] in dict_count2:
#                 dict_count2[s2[i]] += 1
#             else:
#                 dict_count2[s2[i]] = 1
#         dict1_keys = sorted([key for key in dict_count1])
#         dict2_keys = sorted([key for key in dict_count2])
#         if dict1_keys == dict2_keys:
#             for key in dict_count1:
#                 if dict_count1[key] != dict_count2[key]:
#                     return False
#         else:
#             return False    
#         return True

## Approach 2 : Using sorted function 
# def areAnagrams(s1,s2):
#     ss1=sorted(s1)
#     ss2=sorted(s2)
#     return ss1==ss2

## Approach 3 : GFG comments solution
def areAnagrams(s1,s2): 
        if len(s1) != len(s2):
            return False
            
        hashmap = {}
        
        for i in s1:
            hashmap[i] = hashmap.get(i, 0) + 1
            
        for i in s2:
            if i not in hashmap:
                return False
                    
            hashmap[i] -= 1
                
            if hashmap[i] < 0:
                return False
                
        return True
s1 = "geeks"
s2 = "kseeg"

res1 = areAnagrams(s1,s2)
print(f"Input {s1}, {s2}\n Result {res1}")