class Solution:
    def minDist(self, arr, x, y):
        n =len(arr)
        idx_x = -1
        idx_y = -1
        min_dist = float('inf')

        if (x not in arr) or (y not in arr):
            return -1    
        for i in range(n):
            if arr[i] ==x:
                idx_x = i
            if arr[i] == y:
                idx_y = i
            if idx_x!=-1 and idx_y!=-1 and min_dist>abs(idx_x-idx_y):
                min_dist = abs(idx_x-idx_y)
        return min_dist

if __name__=="__main__":
    sol_obj = Solution()

    arr = [1, 2, 3, 2]
    x = 1
    y = 2
    res = sol_obj.minDist(arr,x,y) 
    print(f"Input:{arr}\n Result:{res}")

    arr = [86, 39, 90, 67, 84, 66, 62] 
    x = 42
    y = 12
    res = sol_obj.minDist(arr,x,y) 
    print(f"Input:{arr}\n Result:{res}")

    arr = [10, 20, 30, 40, 50] 
    x = 10
    y = 50

    res = sol_obj.minDist(arr,x,y) 
    print(f"Input:{arr}\n Result:{res}")

