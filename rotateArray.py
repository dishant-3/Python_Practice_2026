# Databricks notebook source
def rotateArray(arr, d):
    """Rotate an array to the right by d positions.

    Args:
        arr (list): The input array.
        d (int): Number of positions to rotate.

    Returns:
        list: The rotated array.
    """
    ## Approach 1 : Brute Force Approach by traversing the array
    # n = len(arr)
    # while d>0:
    #     last_element = arr[n-1]
    #     for i in range(n-1,0,-1):
    #         arr[i]=arr[i-1]
    #     arr[0]=last_element
    #     d=d-1
    # return arr
    
    # n = len(arr)
    # d = d % n  # Handle cases where d > n
    # return arr[-d:] + arr[:-d]

    # Using a temporary array method1
    # n = len(arr)
    # d = d % n  # Handle cases where d > n
    # temp = [0] * n
    # for i in range(n):
    #     new_index = (i + d) % n
    #     temp[new_index] = arr[i]
    # return temp

    ## For left rotation 
    ## new_index = (i - d + n) % n

    # Approach 2: Using temporary array 
    n= len(arr)
    d = d % n  # Handle cases where d > n
    temp = [0]*n

    for i in range(d):
        temp[i]=arr[n-d+i]
    for i in range(n-d):
        temp[i+d]=arr[i]
    return temp

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 3
    print("Original array:", arr)
    rotated = rotateArray(arr, d)
    # print(f"First part :{arr[-d:]}")
    # print(f"Second part :{arr[:-d]}")
    print(f"Array after rotating right by {d} positions:", rotated)