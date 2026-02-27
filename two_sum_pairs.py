class Solution:
	def twoSum(self, arr, target):
        ## Approach 1 : fails for test case when we have target = 0
		# n = len(arr)
		# if n == 1:
		# 	return False
		# li_set = set(arr)
		# for num in arr:
		# 	ele = target-num
		# 	if ele in li_set:
		# 		return True
		# 	else:
		# 		pass
		# return False	
		## https://www.geeksforgeeks.org/dsa/check-if-pair-with-given-sum-exists-in-array/
		seen_set = set()
		for num in arr:
			complement = target -num
			if complement in seen_set:
				return True
			seen_set.add(num)
		return False

if __name__ =="__main__":
	sol_obj = Solution()	
	arr = [0, -1, 2, -3, 1]
	target = -2
	res= sol_obj.twoSum(arr,target)
	print(f"Input:{arr}\t Target:{target}\n Result:{res}")
	arr = [1, -2, 1, 0, 5]
	target = 0
	res= sol_obj.twoSum(arr,target)
	print(f"Input:{arr}\t Target:{target}\n Result:{res}")
	arr = [11]
	target = 11
	print(f"Input:{arr}\t Target:{target}\n Result:{res}")