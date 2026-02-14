# Databricks notebook source
def getOddOccurrence(arr,size):
     
    # Defining HashMap in python
    Hash=dict()
 
    # Putting all elements into the HashMap 
    for i in range(size):
        Hash[arr[i]]=Hash.get(arr[i],0) + 1;
    
    # Iterate through HashMap to check an element
    # occurring odd number of times and return it
    for i in Hash:

        if(Hash[i]% 2 != 0):
            return i
    return -1

if __name__ == "__main__":
    arr=[2, 3, 5, 4, 5, 2, 4,3, 5, 2, 4, 4, 2]
    n = len(arr)
    print(getOddOccurrence(arr, n))