## Approach 1 : Sorting 
# def getSecondLargest(arr):
#         # Code Here
#         sorted_li = list(sorted(set(arr),reverse = True))
#         if len(sorted_li)>1:
#             return sorted_li[1]
#         else:
#             return -1    
# list1 = [0,1,2,3,4,5,7,8]
# list2 = [10,5,10]
# list3 = [10,10,10]

# res1 = getSecondLargest(list1)
# print(f"List 1 res:{res1}")

# res2 = getSecondLargest(list2)
# print(f"List 2 res: {res2}")

# res3 = getSecondLargest(list3)
# print(f"List 3 res: {res3}")

## Approach 2: 
# def getSecondLargest(arr):
#     # Exit if array size is less than 2
#     if len(arr) < 2:
#         return -1
    
#     # Initialise both largest and second largest to -1
#     largest = second = -1
    
#     for num in arr:
#         # If num is greater than largest 
#         # Demote old largest to second largets and assign num as largest
#         if num > largest:
#             second = largest
#             largest = num
#         # If number is greater than second largest and is not equl to largest
#         # The and condition w=check where number is not equal to largest prevents using duplicates
#         elif num > second and num != largest:
#             second = num
    
#     return second if second != -1 else -1

def getSecondLargest(arr):
    if len(arr) < 2:
        return -1
    max1 = max2 = -1
    for n in arr:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2 and n != max1:
            max2 = n
    return max2


list1 = [0,1,2,3,4,5,7,8]
list2 = [1,3,3,3]
list3 = [10,10,10]

res1 = getSecondLargest(list1)
print(f"List 1 res:{res1}")

res2 = getSecondLargest(list2)
print(f"List 2 res: {res2}")

res3 = getSecondLargest(list3)
print(f"List 3 res: {res3}")