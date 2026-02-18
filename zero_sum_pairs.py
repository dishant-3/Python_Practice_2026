def zero_sum_pairs(arr):
    # arr1= sorted(arr)
    n =len(arr)
    li_set = set(arr)
    zero_cnt =0
    for num in arr:
        if num ==0:
            zero_cnt+=1
    # li_set = [ele for ele in li_set if ele !=0]
    # positive_li =[ele for ele in li_set if ele >=0]
    # negative_li =[ele for ele in li_set if ele <0]
    res_set =[]
    for num in li_set:
        if num <0 and -num in li_set and [num,-num] not in res_set :
                res_set.append([num,-num])
            # li_set.remove(num)
        if num ==0 and zero_cnt >1 and [0,0] not in res_set:
            res_set.append([0,0])
    sorted_res = sorted(res_set)
    return sorted_res

# def zero_sum_pairs(arr):
#     n = len(arr)
#     res = []
#     mp = {}

#     for i in range(n):
#         # Check if there exists an element that can pair with arr[i]
#         if -arr[i] in mp:
#             # If such an element exists, iterate through its indices
#             for idx in mp[-arr[i]]:
#                 res.append([idx, i])
        
#         # Store index of the current element in the map
#         if arr[i] in mp:
#             mp[arr[i]].append(i)
#         else:
#             mp[arr[i]] = [i]
    
#     return res

# def zero_sum_pairs(arr):
#     seen = {}
#     result = []
#     zero_count = 0
    
#     for num in arr:
#         if num == 0:
#             zero_count += 1
#             continue
            
#         target = -num
#         if target in seen and [min(num, target), max(num, target)] not in result:
#             result.append([min(num, target), max(num, target)])
        
#         seen[num] = seen.get(num, 0) + 1
    
#     # Add [0,0] only if we have 2+ zeros
#     if zero_count >= 2:
#         result.append([0, 0])
    
#     return sorted(result)


# arr1= [-1, 0, 1, 2, -1, -4]
# res1 = zero_sum_pairs(arr1)
# arr2 = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
# res2 = zero_sum_pairs(arr2)
# arr3 =[1,3,5,-5,-3,-1,0,0]
# res3 = zero_sum_pairs(arr3)
# arr4 = [-8,-10,-10,-10,10,6,1,10]
# res4 = zero_sum_pairs(arr4)
# print(f"Input1 {arr1}\n Result1 {res1}")
# print(f"Input2 {arr2}\n Result2 {res2}")
# print(f"Input3 {arr3}\n Result3 {res3}")
# print(f"Input4 {arr4}\n Result4 {res4}")

# def findAllPairs(arr):
#     n = len(arr)
#     res = []

#     mp = {}

#     for i in range(n):
        
#         # Check if there exists an element that can pair with arr[i]
#         if -arr[i] in mp:
#             # If such an element exists, iterate through its indices
#             # for idx in mp[-arr[i]]:
#             #     res.append([-arr[i], arr[i]])
#             # Add the numbers to result array
#             if [min(-arr[i],arr[i]),max(-arr[i],arr[i])] not in res:
#                 res.append([min(-arr[i],arr[i]),max(-arr[i],arr[i])])
        
#         # Store index of the current element in the map
#         if arr[i] in mp:
#             mp[arr[i]].append(i)
#         else:
#             mp[arr[i]] = [i]
#         # print(f"The map is: {mp} ")    
    
#     return sorted(res)

## Got the below suggestions from GFG Yogi AI
# Suggestion by Your Own GeeksforGeeks Intelligence :
# It looks like your current approach is using a dictionary to track indices of elements, but the way you're checking for pairs and ensuring uniqueness could be optimized. Here are a few hints to help you improve the performance of your code:

# 1. **Use a Set for Uniqueness**: Instead of checking if a pair is already in the result list (`res`), consider using a set to store pairs. This will allow you to automatically handle duplicates without needing to check for their existence.

# 2. **Sort the Array First**: If you sort the array at the beginning, you can simplify the process of finding pairs. This way, you can use a two-pointer technique to find pairs that sum to zero, which can be more efficient than nested loops.

# 3. **Avoid Nested Loops**: The current approach may lead to a time complexity that exceeds O(n log n). By using a two-pointer technique after sorting, you can achieve a linear scan to find pairs, which will significantly reduce the execution time.

# 4. **Directly Append Pairs**: When you find a valid pair, you can directly append it to your result set (or list) in a sorted manner, since you will already have the array sorted.

# By implementing these strategies, you should be able to optimize your code and meet the expected time complexity. Good luck!

## Ai generated code
## optimised code using two pointers
def findAllPairs(arr):
    arr.sort()  # O(n log n) - Suggestion 2
    n = len(arr)
    res = []
    pair_set = set()  # O(1) lookups - Suggestion 1
    
    left, right = 0, n-1
    while left < right:  # Two-pointer O(n) - Suggestion 3
        current_sum = arr[left] + arr[right]
        
        if current_sum == 0:
            pair = [arr[left], arr[right]]
            pair_tuple = tuple(pair)
            if pair_tuple not in pair_set:  # O(1) check
                pair_set.add(pair_tuple)
                res.append(pair)  # Directly append - Suggestion 4
            left += 1
            right -= 1
        elif current_sum < 0:
            left += 1
        else:
            right -= 1
    
    return res

### gfg comment

# class Solution:
#     def getPairs(self, arr):
#         ans = []
#         arr.sort()
#         s = set(arr)
#         used = set()   # to avoid duplicate processing

#         for i in arr:          # keeps sorted order
#             if i in used:
#                 continue

#             j = -i

#             # case (0,0)
#             if i == 0 and arr.count(0) > 1:
#                 ans.append([0, 0])

#             # normal case
#             elif j in s and i < j:
#                 ans.append([i, j])

#             used.add(i)

#         return ans

if __name__ == "__main__":
    arr = [20, 20, -20, 10, -10]
  
    res = findAllPairs(arr)
    # for pair in res:
    #     print(pair[0], pair[1])
    print(f"Input {arr}\n result  {res}")
    arr1= [-1, 0, 1, 2, -1, -4]
    res1 = findAllPairs(arr1)
    print(f"Input1 {arr1}\n Result1 {res1}")
    arr2 = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
    res2 = findAllPairs(arr2)
    print(f"Input2 {arr2}\n Result2 {res2}")
    arr3 =[1,3,5,-5,-3,-1,0,0]
    res3 = findAllPairs(arr3)
    print(f"Input3 {arr3}\n Result3 {res3}")
    arr4 = [-8,-10,-10,-10,10,6,1,10]
    res4 = findAllPairs(arr4)
    print(f"Input4 {arr4}\n Result4 {res4}")