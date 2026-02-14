## Lambda functions are anonymous functions
even_check = lambda x: f"{x} is Even" if x%2 ==0 else f"{x} is Odd"
print(even_check(5))
print(even_check(8))

## Map funtion takes two arguments func1 and iterable
## Map applies func1 to each element of the iterable

str_li = ['1','2','3','4','5']
res = map(int,str_li)
print(f"Map object: {res}")
print(f"Map cast to integers List result: {list(res)}")

def double(val):
    return val*2

a = [1,2,3,4,5]
res = list(map(double,a))
print(f"Map function to double output:{res}")

## Using Lambda function with Map function
a= [1,2,3,4,5]
res = list(map(lambda x: x*2,a))
print(f"The result with map and lambda: {res}")

## We have to give just name of function without () as argument to map function

s = ['  hello  ', '  world ', ' python  ']
res = list(map(str.strip,s))
print(f"Map function to remove whitespces:{res}")
