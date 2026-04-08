# def square_numbers(nums):
#     result =[]
#     for num in nums:
#         result.append(num*num)
#     return result

## Instead of creating a normal function with return statement
## We use yield() function in generators
def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums = square_numbers([1,2,3,4,5])
print("Printing generator object",my_nums)
print(next(my_nums))## next() function can be used to print the results one by one
for num in my_nums:
    print(num)

my_nums2 = (x*x for x in [1,2,3,4,5]) ## Generator expression
## generator expression is an alternate of List comprehension 

print(list(my_nums2)) # [1, 4, 9, 16, 25]

