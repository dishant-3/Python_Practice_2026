# Databricks notebook source
def subarray(arr):
    """Generate all subarrays of a given array.

    Args:
        arr (list): The input array.

    Yields:
        list: Each subarray of the input array.
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield arr[i:j]

#     if __name__ == "__main__":
#         arr = [1, 2, 3, 4]
#         print("All subarrays of the given array:")
#         for subarr in subarray(arr):
#             print(subarr)

def all_subarrays(arr):
    n = len(arr)
    subarrays = []
    for i in range(n):              # starting index
        for j in range(i, n):       # ending index
            subarrays.append(arr[i:j+1])
    return subarrays

# Example usage:
arr = [1, 2, 3]
print(all_subarrays(arr))

def subArrays(arr):
    n=len(arr)
    result_arr=[]
    for i in range(n):
        for j in range(i,n):
            sub_arr=[]
            for k in range(i,j+1):
                sub_arr.append(arr[k])
            result_arr.append(sub_arr)
    return result_arr
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print("All subarrays of the given array:")
    my_res=subArrays(arr)
    for subarr in my_res:
        print(subarr)

