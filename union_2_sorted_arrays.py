class Solution:
    def findUnion(self,a,b):
        # set_a = set(a)
        # set_b = set(b)
        # res_li =[]

        # for ele in set_a:
        #     if ele not in res_li:
        #         res_li.append(ele)
        # for ele in set_b:
        #     if ele not in res_li:
        #         res_li.append(ele)
        # return res_li
        count_dict = {}
        res_li =[]
        for ele in a:
            count_dict[ele]=count_dict.get(ele,0)+1
        for ele in b:
            count_dict[ele]=count_dict.get(ele,0)+1
        for key in count_dict.keys():
            res_li.append(key)
        return res_li

sol_obj = Solution()

a = [1, 2, 3, 4, 5] 
b= [1, 2, 3, 6, 7]
res = sol_obj.findUnion(a,b)
print(res)

