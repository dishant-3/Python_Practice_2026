def checkEqual(a,b):
        count_dict = {}
        # count_dict2 = {}
        
        for ele in a:
           count_dict[ele] = count_dict.get(ele,0)+1
        print(f"count_dictionary after first array:{count_dict}")
        for ele in b:
            if ele not in count_dict:
                return False
            
            count_dict[ele]-=1
            print(f"Count dictinary before False:{count_dict}")
            if count_dict[ele] <0:
                return False
        return True

a1 = [1,2,5,4,0]
b1 = [2,4,5,0,1]
res1 = checkEqual(a1,b1)
print(f"Inputs :{a1}\n{b1} result: {res1}")

