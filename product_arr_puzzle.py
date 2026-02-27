from loguru import logger
class Solution:
    def productExceptSelf(self, arr):
        ## Approach 1: Incorrect solution
        # prod_res =1
        # n = len(arr)
        # res_arr=[]
        # zero_flag = False
        # for num in arr:
        #     if num ==0:
        #         zero_flag = True
        #     else:
        #         prod_res = prod_res*num
        # logger.info(f"The product :{prod_res}")

        # for i in range(n):
        #     try:
        #         # prod_res = prod_res//arr[i]
        #         if zero_flag== True and arr[i] !=0:
        #             res_arr.append(0)
        #         else:
        #             res_arr.append(prod_res//arr[i])
        #     except ZeroDivisionError:
        #         res_arr.append(prod_res)

        # return res_arr
        ## Approach 2: Naive Solution
        # n = len(arr)
        # res_arr = []
        # for i in range(n):
        #     prod_res = 1
        #     for j in range(n):
        #         if i ==j:
        #             pass
        #         else:
        #             prod_res = prod_res * arr[j]
        #     res_arr.append(prod_res)
        # return res_arr

        ## Approach 3:
        n = len(arr)
        
        # Step 1: prefix products
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * arr[i-1]
        
        # Step 2: suffix products
        suffix = [1] * n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * arr[i+1]
        
        # Step 3: result = prefix * suffix
        res = [prefix[i] * suffix[i] for i in range(n)]
        return res

    
if __name__=="__main__":
        
    sol_obj = Solution()
    arr = [10, 3, 5, 6, 2]
    res=sol_obj.productExceptSelf(arr)
    logger.info(f"Input{arr}\n Result{res}")
    arr =[12,0]
    res=sol_obj.productExceptSelf(arr) 
    logger.info(f"Input{arr}\n Result{res}")
    arr = [12,0,3,0]
    res = sol_obj.productExceptSelf(arr)
    logger.info(f"Input{arr}\n Result{res}")

