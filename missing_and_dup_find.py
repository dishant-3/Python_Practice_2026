def find_dup_and_missing(arr):
        n = len(arr)
        counter_dict = {}
        res_arr =[]
        dup_ele = -9999
        miss_ele = -9999
        ## Initialise each element count to zero in counter dictionary
        for i in range(n):
            counter_dict[i+1] = 0
        # print(f"Raw Counter Dictionary \n{counter_dict}")    
        
        for num in arr:
            counter_dict[num] +=1
        print(f"updated counter dictionary \n{counter_dict}")

        for key,val in counter_dict.items():
            if val > 1:
                # res_arr.append(key)
                dup_ele = key
                print(f"Duplicate element: {key}")
            if val == 0:
                # res_arr.append(key)
                miss_ele =key
                print(f"Missing element:{key}")
        res_arr.append(dup_ele)
        res_arr.append(miss_ele)
        return res_arr

arr1 =[2,2]
res1= find_dup_and_missing(arr1)
print(f"Result is : {res1}")

arr2 = [1,3,3]
res2 = find_dup_and_missing(arr2)
print(f"Result is : {res2}")

arr3 = [4, 3, 6, 2, 1, 1]
res3 = find_dup_and_missing(arr3)
print(f"Result is : {res3}")