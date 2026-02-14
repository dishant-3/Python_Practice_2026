## Approach1: Using dictionary to store count 
# def find_dups(arr):
#     counter_dict ={}
#     for num in arr:
#         if num not in counter_dict:
#             counter_dict[num] = 1
#         else:
#             counter_dict[num] +=1
#     dups_arr =[]
#     for num,value in counter_dict.items():
#         if value>1:
#             dups_arr.append(num)
#     return dups_arr
# a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
# res=find_dups(a)
# print(res)

## approach 2 Using collections library

# from collections import Counter

# def find_duplicates(arr):
#     count_dict = Counter(arr)
#     return [num for num, cnt in count_dict.items() if cnt > 1]

# # Test
# arr = [1, 3, 4, 2, 2, 4, 1]
# print(find_duplicates(arr))  # [1, 2, 4]

## Approach 3 using set library
my_arr = [1, 2, 3, 1, 2, 4, 5, 6, 5]
my_set = set()
dups=[]

for n in my_arr:
    if n in my_set:
        dups.append(n)
    else:
        my_set.add(n)
print(f"Duplicates : {dups}")


## Counter is a very powerful library

# from collections import Counter
# arr = [1, 3, 4, 2, 2, 4, 1]
# count_dict = Counter(arr)
# print(count_dict)  # Counter({1: 2, 2: 2, 4: 2, 3: 1})

# Counter does this automatically:
# count_dict = {}
# for num in arr:
#     count_dict[num] = count_dict.get(num, 0) + 1

# c = Counter([1, 2, 2])
# print(c[1])  # 1
# print(c[3])  # 0 (not  KeyError!)
