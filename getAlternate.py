# Databricks notebook source
def getAlternate(arr):
    result = []
    for i in range(0, len(arr), 2):
        result.append(arr[i])
    return result

if __name__ == "__main__":
    arr = [10,20,30,40,50]
    print("Length of array:", len(arr))
    res = getAlternate(arr)
    print(" ".join(map(str,res)))
    