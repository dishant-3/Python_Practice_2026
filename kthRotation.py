## Approach 1 : The index of minimum element is the no of rotations
# def findkth_Rotation(arr): 
#     n = len(arr)
#     min_ele = arr[0]
#     rotate_res = 0
#     for i in range(n):
#         if arr[i]<min_ele:
#             min_ele = arr[i]
#             rotate_res = i
#     return rotate_res

## Aproach 2 : The only occassion in an array where 
## a larger element is followed by a smaler element

def findkth_Rotation(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return i+1
    return 0
arr1 =  [6, 9, 2, 4]
res1 = findkth_Rotation(arr1)
print(f"Count of rotations: {res1}")
arr2 = [5, 1, 2, 3, 4]
res2 = findkth_Rotation(arr2)
print(f"Count of rotations: {res2}")