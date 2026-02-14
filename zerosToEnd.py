# Databricks notebook source
def pushZerosToEnd(arr):
    """Move all zeros in the array to the end while maintaining the order of non-zero elements.

    Args:
        arr (list): The input array.

    Returns:
        list: The array with zeros moved to the end.
    """
    # ## Approach 1: Using a temporary array
    # n = len(arr)
    # count = 0  # Count of non-zero elements
    # temp = [0] * n
    # # Traverse the array. If element is non-zero, then
    # # replace the element at index 'count' and increment 'count'
    # for i in range(n):
    #     if arr[i] != 0:
    #         temp[count] = arr[i]
    #         count += 1

    # # Now all non-zero elements have been shifted to
    # # front and 'count' is set as index of first 0.
    # # Make all elements 0 from count to end.
    # while count< n:
    #     temp[count] = 0
    #     count += 1

    # return temp
    
    # # ## Approach 2: In-place modification
    # n = len(arr)
    # count = 0  ## index for next non-zero element
    # for i in range(n):
    #     if arr[i] != 0:
    #         arr[count] = arr[i]
    #         count += 1
    # while count < n:  ## Now make all the remaining elements in the array zero
    #     arr[count] = 0
    #     count += 1
    # # return arr
    
    ## Approach3: In-place swap
    n = len(arr)
    j = 0  # Pointer for the next non-zero element position
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    # return arr
if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    # res_arr = pushZerosToEnd(arr)
    # print(f"Array after moving zeros to the end:{res_arr}")
    pushZerosToEnd(arr)

    for i in arr:
        print(i, end=" ")