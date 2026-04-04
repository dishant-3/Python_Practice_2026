# class Solution:
#     def findUnion(self,a,b):
#         # set_a = set(a)
#         # set_b = set(b)
#         # res_li =[]

#         # for ele in set_a:
#         #     if ele not in res_li:
#         #         res_li.append(ele)
#         # for ele in set_b:
#         #     if ele not in res_li:
#         #         res_li.append(ele)
#         # return res_li
#         count_dict = {}
#         res_li =[]
#         for ele in a:
#             count_dict[ele]=count_dict.get(ele,0)+1
#         for ele in b:
#             count_dict[ele]=count_dict.get(ele,0)+1
#         for key in count_dict.keys():
#             res_li.append(key)
#         return res_li

# sol_obj = Solution()

# a = [1, 2, 3, 4, 5] 
# b= [1, 2, 3, 6, 7]
# res = sol_obj.findUnion(a,b)
# print(res)
##### TUF Solution 1: Using set union operation 
class Solution:
    # Function to find the union of two arrays using set
    def findUnion(self, arr1, arr2):
        # Create a set with elements from both arrays
        st = set(arr1) | set(arr2)  # Union of two sets

        # Return sorted list
        return sorted(st)

# Driver code
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

obj = Solution()
result = obj.findUnion(arr1, arr2)

print("Union of arr1 and arr2 is:", *result)

####### TUF Solution 2: Two Pointer Algorithm
class Solution:
    # Function to find union of two sorted arrays using two pointers
    def findUnion(self, arr1, arr2, n, m):
        # List to store union elements
        Union = []

        # Initialize pointers
        i, j = 0, 0

        # Iterate while both pointers are within array bounds
        while i < n and j < m:
            # If element in arr1 is smaller
            if arr1[i] < arr2[j]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
            # If element in arr2 is smaller
            elif arr2[j] < arr1[i]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr2[j]:
                    Union.append(arr2[j])
                j += 1
            else:
                # Elements are equal, add once if not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
                j += 1

        # Append remaining elements from arr1
        while i < n:
            if not Union or Union[-1] != arr1[i]:
                Union.append(arr1[i])
            i += 1

        # Append remaining elements from arr2
        while j < m:
            if not Union or Union[-1] != arr2[j]:
                Union.append(arr2[j])
            j += 1

        # Return the union list
        return Union


# Driver code
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    n, m = len(arr1), len(arr2)

    obj = Solution()
    result = obj.findUnion(arr1, arr2, n, m)
    print("Union of arr1 and arr2 is:", *result)


