# Databricks notebook source
def revArray1(arr):
    """ reverse an array using slicing """      
    # arr[::-1]
    return arr[::-1]
def revArray2(arr):
    """ reverse an array using two pointer approach """
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
def revArray3(arr):
    """ reverse an array using temp array """
    n = len(arr)
    temp = [0]*n
    for i in range(n):
        temp[i] = arr[n-i-1]
    return temp
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    print("Reversed array using slicing:", revArray1(arr))
    arr = [1, 2, 3, 4, 5]
    print("Reversed array using two pointer approach:", revArray2(arr))
    arr = [1, 2, 3, 4, 5]
    print("Reversed array using temp array:", revArray3(arr))