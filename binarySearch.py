# Databricks notebook source
# # Approach 1: Iterative Binary search

def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    result -1
    while low <= high:
        mid = low + (high-low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            result = mid    ## Added this to find first occurence
            high = mid-1
        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        else:
            high = mid - 1
    return result
if __name__ == '__main__':
    # arr = [2, 3, 4, 10, 40]
    arr = [1,1,1,2,2,3,3,3,3,3,3,4,4,4,5,5,5]
    x = 3

    result = binarySearch(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

###  Approach 2: Recursive Binary search
# def binarySearch(arr, x, low=0, high=None):
#     if high is None:
#         high = len(arr) - 1

#     # Base case: If the range is invalid
#     if low > high:
#         return -1

#     mid = low + (high - low) // 2

#     # Check if x is present at mid
#     if arr[mid] == x:
#         return mid
#     # If x is smaller, search in the left half
#     elif arr[mid] > x:
#         return binarySearch(arr, x, low, mid - 1)
#     # If x is greater, search in the right half
#     else:
#         return binarySearch(arr, x, mid + 1, high)

