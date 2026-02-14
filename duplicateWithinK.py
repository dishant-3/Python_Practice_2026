# Databricks notebook source
## Check if an element is duplicate within k distance in an array
# Python 3 program to Check if a given array 
# contains duplicate elements within k distance
# from each other 
## Approach 1: Naive approach
def checkDuplicatesWithinK(arr,n,k):
    for i in range(n):
        j =i+1
        while j+k<=n:
            for ele in range(j,j+k):
                subarray=arr[j:j+k]
                print("My Subarray is",subarray)
                flag =0
                if arr[i] in subarray:
                    flag=1
                else:
                    pass
                print("Flag is ",flag)

 


# ## Approach 2: Using set
# def checkDuplicatesWithinK(arr, n, k):

#     # Creates an empty list
#     myset = set()

#     # Traverse the input array
#     for i in range(n):
    
#         # If already present n hash, then we 
#         # found a duplicate within k distance
#         if arr[i] in myset:
#             return True

#         # Add this item to hashset
#         myset.add(arr[i])

#         # Remove the k+1 distant item
#         if (i >= k):
#             myset.remove(arr[i - k])
#     return False

# Driver Code
if __name__ == "__main__":
    
    arr = [10, 5, 3, 4, 3, 5, 6]
    n = len(arr)
    if (checkDuplicatesWithinK(arr, n, 3)):
        print("Yes Duplicate is present")
    else:
        print("No duplicate found within k")