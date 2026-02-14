## Approach 1: Brute Force Approach

# def find_equi(arr):
#     for i in range(len(arr)):
#         left_arr = arr[:i]
#         right_arr = arr[i+1:]
#         if sum(left_arr) == sum(right_arr):
#             return i
#     return -1

# arr1 = [1, 1, 1, 1]
# arr2=[-7, 1, 5, 2, -4, 3, 0]
# arr3 = [1, 2, 0, 3]
# res1=find_equi(arr1)
# res2=find_equi(arr2)
# res3=find_equi(arr3)
# print(f"Input: {arr1} \n Result is :{res1}")
# print(f"Input: {arr2} \n Result is :{res2}")
# print(f"Input: {arr3} \n Result is :{res3}")

## Approach 2: using right and left prefix sum of arrays

# def findEquilibrium(arr):
#     n = len(arr)

#     pref = [0] * n
#     suff = [0] * n

#     # Initialize the ends of prefix and suffix array
#     pref[0] = arr[0]
#     suff[n - 1] = arr[n - 1]

#     # Calculate prefix sum for all indices
#     for i in range(1, n):
#         pref[i] = pref[i - 1] + arr[i]

#     # Calculating suffix sum for all indices
#     for i in range(n - 2, -1, -1):
#         suff[i] = suff[i + 1] + arr[i]

#     # Checking if prefix sum is equal to suffix sum
#     for i in range(n):
#         if pref[i] == suff[i]:
#             return i 

#     # if equilibrium index doesn't exist
#     return -1
  
# if __name__ == "__main__":
#     arr = [-7, 1, 5, 2, -4, 3, 0]

#     print(findEquilibrium(arr))

## In the approach 2 it is the below equation
## arr[0:3]+ arr[3] = arr[3] + arr[4:]
## Both the arr[3] variables get cancelled in LHS and RHS
