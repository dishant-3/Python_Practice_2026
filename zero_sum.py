## Approach 1 : Using set in python

# def add_num(li):
#     l1 = set(li)
#     for i in li:
#         if -i in l1:
#             return True
#         else:
#             pass
#     return False

# my_list = [1,2,3,4,0,-1,-2]

# res=add_num(my_list)


# if res:
#     print("Two numbers with zero sum exist")
# else:
#     print("No zero sum numbers exist")

## Approach 2: brute force approach
my_list = [1,2,3,4,0,-1,-2]
def zer_sum_pair(my_list):
    for i in range(len(my_list)):
            for j in range(i+1,len(my_list)):
                 if my_list[i]+my_list[j]==0:
                      return [i,j]
                 else:
                      pass
    return []
res = zer_sum_pair(my_list)

if res:
    print(f"Two numbers with zero sum exist at index {res}")
else:
    print("No zero sum numbers exist")