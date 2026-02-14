# Databricks notebook source
# # Sol1:
# def leaders(arr):
#     res_arr=[]
#     n = len(arr)

#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]<arr[j]:
#                 break
#         if j==n-1:
#             res_arr.append(arr[i])
#     return res_arr


# if __name__ == "__main__":
#     arr = [16, 17, 4, 3, 5, 2]
#     print("Length of array:", len(arr))
#     print("Leaders in the array are: ")
#     print(" ".join(map(str,leaders(arr))))

# Sol2


# def leaders(arr):
#     result_arr=[]
#     n= len(arr)
#     max_from_right=arr[n-1]
#     result_arr.append(max_from_right)
#     for i in range(n-2,-1,-1):
#         if arr[i]>max_from_right:
#             max_from_right=arr[i]
#             result_arr.append(max_from_right)
#     result_arr.reverse()
#     return(result_arr)


## Approach 1 : Brute Force approach 
### Navigating Left to Right

# def all_leaders(arr):
#     leaders_arr=[]
#     arr_len = len(arr)
#     if arr_len==2 and arr[1]>arr[0]:
#         leaders_arr.append(arr[1])
#         return leaders_arr
#     elif arr_len ==1:
#         # leaders_arr.append(arr[0])
#         return(arr)
#     else:
#         for i in range(arr_len):
#             broken = False
#             for j in range(i+1,arr_len):
#                 if arr[j]>arr[i]:
#                     broken = True
#                     break
#             if not broken:
#                 leaders_arr.append(arr[i])
#         return leaders_arr
# if __name__ == "__main__":
#     # arr = [16, 17, 4, 3, 5, 2]
#     arr = [51,87]
#     print("Length of array:", len(arr))
#     print("Leaders in the array are: ")
#     my_res=all_leaders(arr)
#     print(" ".join(map(str,my_res)))
    

## Approach 2: Navigating Right to Left
def leaders(arr):
    result = []
    n = len(arr)

    # Start with the rightmost element
    maxRight = arr[-1]

    # Rightmost element is always a leader
    result.append(maxRight)

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= maxRight:
            maxRight = arr[i]
            result.append(maxRight)

    # Reverse the result list to maintain
    # original order
    result.reverse()

    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leaders(arr)
    print(" ".join(map(str, result)))
    



