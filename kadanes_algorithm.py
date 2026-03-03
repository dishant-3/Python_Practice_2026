class Solution:
    def maxSubarraySum(self, arr):
        ### Solution 1 : In this solution I hae tried to reduce the window when my condition fails
        ### It will not work if the first element in the array is positive
        ### Incorrect solution - Sliding window approach
        # n =len(arr)
        # left = 0
        # right = 0
        # curr_sub_sum = arr[0]
        # max_subarr_sum = curr_sub_sum 
        # for i in range(n-1):
        #     right = i+1
        #     curr_sub_sum = sum(arr[left:right+1])
        #     max_subarr_sum = max(curr_sub_sum,max_subarr_sum)
        #     # print(f"left_idx:{left}\t right_idx:{right}\t curr_sum:{curr_sub_sum}\t max_sum:{max_subarr_sum}")
        #     if curr_sub_sum < max_subarr_sum:
        #         left +=1
        # return max_subarr_sum   
    ## brute force approach: Big O(n3)
        # n =len(arr)
        # maxi = float('-inf')
        # for i in range(n):
        #     for j in range(i,n):
        #         sub_arr_sum =0
        #         for k in range(1,j+1):
        #             sub_arr_sum += arr[k]
        #         maxi = max(maxi,sub_arr_sum)
        # return maxi
    ## Brute Force approach: Big O(n2)
        # n = len(arr)
        # maxi = float('-inf')

        # for i in range(n):
        #     sub_arr_sum = 0
        #     for j in range(i,n):
        #         sub_arr_sum += arr[j]   ## Running sum variable
        #         ## We do not use third loop because we are directly adding next element of array to previous sum
        #         maxi = max(maxi,sub_arr_sum)

        # return maxi 
        n = len(arr)
        maxi = float('-inf')
        sum = 0
        for i in range(n):
            sum += arr[i]

            if sum >maxi:
                maxi=sum
            if sum <0:
                sum =0
        return maxi

sol_obj= Solution()
# arr = [2, 3, -8, 7, -1, 2, 3]
# res = sol_obj.maxSubarraySum(arr)
# print(f"Input:{arr}\t Result:{res}")

# arr = [-2, -4]
# res = sol_obj.maxSubarraySum(arr)
# print(f"Input:{arr}\t Result:{res}")

# arr = [5, 4, 1, 7, 8]
# res = sol_obj.maxSubarraySum(arr)
# print(f"Input:{arr}\t Result:{res}")

arr = [1, 2, 3, -2, 5]
res = sol_obj.maxSubarraySum(arr)
print(f"Input:{arr}\t Result:{res}")

arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
res = sol_obj.maxSubarraySum(arr)
print(f"Input:{arr}\t Result:{res}")