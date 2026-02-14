# Databricks notebook source
#Sol2:

# if __name__ == "__main__":
#     arr = [1, 2, 3, 4, 5]
#     n = len(arr)
#     flag = True
#     for i in range(n - 1):
#         if arr[i] > arr[i + 1]:
#             flag = False
#             break
#     if flag:
#         print("The array is sorted in ascending order")
#     else:
#         print("The array is not sorted in ascending order")

if __name__ == "__main__":
    arr = [10,11,12,13,14,15,16]
    n= len(arr)
    flag = True
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            flag = False
            break
    if flag:
        print("The array is sorted in ascending order")
    else:
        print("The array is not sorted in ascending order")