class Solution:
    def transitionPoint(self, arr): 

        ## Approach 1: Complete traversal 
        ## Time Compplexity: O(n)
        # n = len(arr)
        # ## If all the elements are zero
        # if arr[n-1] ==0:
        #     return -1
        # ##If all the elements are one or both zeros and ones are present
        # for i in range(n):
        #     if arr[i] == 1:
        #         return i

        ## Approach 2: Binary search 
        n = len(arr)
        high = n-1
        low = 0
        search_ele = 1 
        res_idx = 0
        if arr[n-1]==0:
            return -1
        if arr[0] ==1:
            return res_idx
        while low<=high:
            mid = low + (high-low)//2
            if arr[mid] == search_ele:
                res_idx = mid
                high =mid-1
            elif arr[mid] < search_ele:
                low = mid+1
            else:
                high = mid-1
        return res_idx



            
if __name__=="__main__":
    sol_obj = Solution()
    arr = [0, 0, 0, 1, 1]
    res =sol_obj.transitionPoint(arr)
    print(f"Input:{arr}\n Output:{res}")
    
    arr = [1, 1, 1]
    res =sol_obj.transitionPoint(arr)
    print(f"Input:{arr}\n Output:{res}")
    
    arr = [0, 0, 0, 0]
    res =sol_obj.transitionPoint(arr)
    print(f"Input:{arr}\n Output:{res}")

    arr = [0, 1, 1]
    res =sol_obj.transitionPoint(arr)
    print(f"Input:{arr}\n Output:{res}")
    
    arr = [0, 0, 0, 0, 1, 1, 1, 1]
    res=sol_obj.transitionPoint(arr)
    print(f"Input:{arr}\n Output:{res}")
