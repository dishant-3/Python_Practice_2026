
## Brute force Approach : traversing array using two loops
# def firstRepeated(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]== arr[j]:
#                 return i+1
#     return -1
# arr1 = [1, 5, 3, 4, 3, 5, 6]
# res1 = firstRepeated(arr1)
# print(f"Input:{arr1}\n Output:{res1}")
# arr2 = [1, 2, 3, 4]
# res2 = firstRepeated(arr2)
# print(f"Input:{arr2}\n Output:{res2}")

## Approach 2: Using Hashmap to count frequency of elements

def firstRepeated(arr):
    counter_dict={}
    n = len(arr)
    for ele in arr:
        counter_dict[ele] = counter_dict.get(ele,0)+1
    
    for i in range(n):
        if counter_dict[arr[i]]>1:
            return i+1
    
    return -1

arr1 = [1, 5, 3, 4, 3, 5, 6]
res1 = firstRepeated(arr1)
print(f"Input:{arr1}\n Output:{res1}")
arr2 = [1, 2, 3, 4]
res2 = firstRepeated(arr2)
print(f"Input:{arr2}\n Output:{res2}")

## For finding first repeating character in a string

def firstRepChar(s):
    # Create an array to store the count of characters
    charCount = [0] * 26

    # Iterate through each character in the string
    for ch in s:

        # Calculate the index in the array for this character
        index = ord(ch) - ord('a')

        # If the count of the character is not zero,
        # it means the character is repeated, so we return it
        if charCount[index] != 0:
            return ch

        # Increment the count of the character in the array
        charCount[index] += 1

    # If no character is repeated, return "-1"
    return "-1"


# Example usage:
s = "geeksforgeeks"
print(firstRepChar(s))