## Remove duplicates from sorted array

## Approach 0: Creating new array and storing results in it
def removeDups(arr):
    
    n = len(arr)
    res_arr =[]
    if n ==0:
        return []
    write_idx=1
    # res_arr[0] = arr[0]
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[write_idx] = arr[i]
            write_idx+=1
    for i in range(write_idx):
        res_arr.append(arr[i])      
    # return arr[:write_idx]
    return res_arr

## Approach 1 : Iteratng through the sorted array and checking with prev element
# def removeDuplicates(arr):
#     if not arr:
#         return 0

#     write_index = 1

#     for i in range(1, len(arr)):
#         if arr[i] != arr[i - 1]:
#             arr[write_index] = arr[i]
#             write_index += 1

#     return write_index
def removeDuplicates(arr):
    seen_elements = set()

    new_size =0
    for i in range(len(arr)):
        if arr[i] not in seen_elements:
            seen_elements.add(arr[i])
            arr[new_size]=arr[i]
            new_size+=1
    return new_size

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    # newSize = removeDuplicates(arr)
    # print("Result using approach 1\n")
    # for i in range(newSize):
    #     print(arr[i], end=" ")

    result = removeDups(arr)
    print(f"\n Result using approach zero:{result}")
