# Databricks notebook source
def minOps(arr, n, k):
    max_val = max(arr)
    res =0

    for i in range(0,n):
        if ((max_val - arr[i]) % k != 0):
            return -1
        else:
            res += (max_val - arr[i]) / k
    return int(res)
# driver program
arr = [21, 33, 9, 45, 63] 
n = len(arr)
k = 6
print(minOps(arr, n, k))