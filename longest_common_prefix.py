## Approach 1: Using sorting
def longestCommonPrefix(arr):
    arr.sort()
    res_str =""
    if len(arr) ==0:
        return res_str
    first = arr[0]
    last = arr[-1]

    min_len = min(len(first),len(last))
    if min_len != 0:
        res_arr=[]
        for i in range(min_len):
            if first[i] == last[i]:
                res_arr.append(first[i])
            else:
                # print(f"Character mismatch found at index :{i}")
                # print(f"Before join method:{res_str}")
                
                
                break
                # print(f"After join method:{res_str}")
        res_str ="".join(res_arr)
    return res_str

arr1 = ["geeksforgeeks", "geeks", "geek", "geezer"]
arr2 = ["interview", "internet", "internal", "interval"]
arr3 = ["hello", "world"]


res1 = longestCommonPrefix(arr1)
print(f"Input:{arr1}\n Result:{res1}")

res2 = longestCommonPrefix(arr2)
print(f"Input:{arr2}\n Result:{res2}")

res3 = longestCommonPrefix(arr3)
print(f"Input:{arr3}\n Result:{res3}")

## TUF Code
class Solution:
    # Returns the longest common prefix from a list of strings
    def longestCommonPrefix(self, strs):
        # Handle empty list case
        if not strs:
            return ""
        
        # Sort the list lexicographically
        strs.sort()
        
        # First string in sorted list
        first = strs[0]
        
        # Last string in sorted list
        last = strs[-1]
        
        # Store the common prefix characters
        ans = []
        
        # Compare characters of first and last string
        for i in range(min(len(first), len(last))):
            # Stop if characters differ
            if first[i] != last[i]:
                return ''.join(ans)
            # Add matching character to result
            ans.append(first[i])
        
        # Return the longest common prefix
        return ''.join(ans)

# # Run the function with sample input
# if __name__ == "__main__":
#     # Create an instance of Solution
#     solution = Solution()
    
#     # Input list of strings
#     input_strs = ["interview", "internet", "internal", "interval"]
    
#     # Call the method to find prefix
#     result = solution.longestCommonPrefix(input_strs)
    
#     # Print the result
#     print("Longest Common Prefix:", result)  

## https://www.geeksforgeeks.org/dsa/longest-common-prefix-using-sorting/

