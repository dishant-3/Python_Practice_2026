## Scenario 1: Constant window
## Problem - Find the max sum of continuous elements from given array with fixed window size 

def max_subarray_sum(arr,window_size):
    
    n = len(arr)
    left =0
    window_size -=1
    right = left +window_size
    window_sum = 0
    for i in range(left,right+1):
        window_sum  += arr[i]
    max_win_sum =0
    while right < n-1:
        window_sum = window_sum -arr[left]
        left+=1
        right+=1
        window_sum = window_sum +arr[right]
        print(f"left:{left}\t right:{right} \t window_sum:{window_sum}")
        max_win_sum =max(max_win_sum,window_sum)
    return max_win_sum

arr = [-1,1,2,3,4,5,-1]
res = max_subarray_sum(arr,4)
print(f"Result:{res}")      

        
## Scenario 2: Longest subarray where <condition>
## Longest subarray with sum <= k

## Approach 1: Brute Force approach
## Traverse the array using two loops and find all the subarrays
## Check the condition and return the result
# 
## Approach 2 : Variable size Sliding window 
# We increase the right index till our condition is true
# When our condition is false then we reduce windw size by increasing the left index
# Then we continue to increase the right index in step 1 till our condition is true.
# Finally return result

## Scenario 3: Number of subarrays where condition
# The problems are tobe solved using 

## Scenario 4: Shortest/Minimum window where condition

