class Solution:
    def subarraySum(self, arr, target):
        ## Approach 1 : Naive Solution 
        # n = len(arr)
        # res_arr =[]
        # for i in range(n):
        #     for j in range(i+1,n):
        #         temp_sum = sum(arr[i:j+1])
        #         # print(f"i:{i}\t j:{j} \t sum:{temp_sum}")
        #         if temp_sum == target:
        #             res_arr.append([i+1,j+1])
        #             # return res_arr
        # if len(res_arr)==0:
        #     res_arr.append([-1])
        # return res_arr[0]
    
    ## Approach 2: Sliding Window technique
        n = len(arr)
        left,right =0,0
        current_sum =0
        for right in range(n):
            current_sum += arr[right]

            while current_sum> target and left <= right:
                current_sum -= arr[left]
                left +=1
            
            if current_sum == target:
                return[left+1,right+1]
            
        return [-1]
    
        
if __name__== "__main__":
    sol_obj  = Solution()
    
    arr = [1, 2, 3, 7, 5]
    target = 12
    res = sol_obj.subarraySum(arr,target)
    print(f"result array is:{res}")