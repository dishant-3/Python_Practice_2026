## Approach 1: Brute force

# def miss_num(my_list):
#     ele_miss_flag = False 
#     max_val = max(my_list)
#     correct_list = list(range(max_val+1))
#     print(f"Input list: {my_list}")
#     print(f"Correct list: {correct_list}")
#     for ele in correct_list:
#         if ele in my_list:
#             pass
#         else:
#             ele_miss_flag = True
#             return ele
#     if ele_miss_flag == False:
#         return -99999


# list1 = [0,1,2,3,4,5,7,8]
# list2 = [1,2,3,4,5,6,7,8]
# list3 = [0,1,2,3,4,5,6,7]

# res1 = miss_num(list1)
# print(f"Missing number {res1}")

# res2 = miss_num(list2)
# print(f"Missing number {res2}")

# res3= miss_num(list3)
# print(f"Missing number {res3}")


## Approach 2 : Sum of n integers

def missing_num(arr):
    n = len(arr)
    print(f"Input array: {arr} \n Length of array:{n}")

    # Actual sum
    total_sum= sum(arr)
    print(f"Sum of input array:{total_sum}")
    # Expected sum of array 
    expected_sum = n*(n+1)//2
    print(f"Expected sum of array:{expected_sum}")
    return expected_sum - total_sum

if __name__=='__main__':
    list1 = [0,1,2,3,4,5,7,8]
    list2 = [1,2,3,4,5,6,7,8]
    list3 = [0,1,2,3,4,5,6,7]

    res1 = missing_num(list1)
    print(f"Missing number: {res1}")

    res2 = missing_num(list2)
    print(f"Missing number: {res2}")

    res3= missing_num(list3)
    print(f"Missing number: {res3}")

### Incorrect result

# def miss_num(my_list):
#     ele_miss_flag = False 
#     li_length = len(my_list)
#     correct_list = list(range(li_length+1))
#     print(f"Input list: {my_list}")
#     print(f"Correct list: {correct_list}")
#     for ele in correct_list:
#         if ele in my_list:
#             pass
#         else:
#             ele_miss_flag = True
#             return ele
#     if ele_miss_flag == False:
#         return -99999


# list1 = [0,1,2,3,4,5,7,8]
# list2 = [1,2,3,4,5,6,7,8]
# list3 = [0,1,2,3,4,5,6,7]

# res1 = miss_num(list1)
# print(f"Missing number {res1}")

# res2 = miss_num(list2)
# print(f"Missing number {res2}")

# res3= miss_num(list3)
# print(f"Missing number {res3}")