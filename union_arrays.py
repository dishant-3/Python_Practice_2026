def findUnion(a,b):
    combined_li = a+b
    union_res = list(set(combined_li))
    return union_res

a1 = [1, 2, 3, 2, 1]
b1 = [3, 2, 2, 3, 3, 2]
res1 = findUnion(a1,b1)
print(f"Input\n a:{a1} \n b:{b1} \n Result:{res1}")

a2 = [1, 2, 3] 
b2 = [4, 5, 6]
res2 = findUnion(a2,b2) 
print(f"Input\n a:{a2} \n b:{b2} \n Result:{res2}")

a3 = [1, 2, 1, 1, 2] 
b3 = [2, 2, 1, 2, 1] 
res3 = findUnion(a3,b3)
print(f"Input\n a:{a3} \n b:{b3} \n Result:{res3}")