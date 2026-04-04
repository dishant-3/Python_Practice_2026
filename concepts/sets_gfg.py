def setInsert(arr, n):
    #code here
    my_set = set()
    for ele in arr:
        my_set.add(ele)
    return my_set
        

def setDisplay(s):
    #code here
    for ele in sorted(s):   ## sorted() fucntion returns a sorted list of elements
        print(ele,end=" ")
    print()

def setErase(s, x):
    #code here  ## remove() function would throw an error
    if x in s:
        s.discard(x)    ##  discard() function removes the element from set without raising error 
        print(f"erased {x}")
    else:
        print("not found")

## Driver code
n = 10
arr = [9,8,7,4,4,2,1,1,9,8]
x = 1
my_set=setInsert(arr,n)
setDisplay(s=my_set)
setErase(s=my_set,x=x)
print(f"After erasing element:{my_set}")

## Union Operation
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '|' operator
res1 = A | B
print("using '|':", res1)

# Using union() method
res2 = A.union(B)
print("using union():",res2)

## Intersection Operation

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '&' operator
res1 = A & B
print("using '&':",res1)

# Using intersection() method
res2 = A.intersection(B)
print("using intersection():",res2)

## Difference Operation
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '-' operator
res1 = A - B
print("using '-':", res1)

# Using difference() method
res2 = A.difference(B)
print("using difference():", res2)

## Symmetric Difference of Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '^' operator
res1 = A ^ B
print("using '^':", res1)

# Using symmetric_difference() method
res2 = A.symmetric_difference(B)
print("using symmetric_difference():", res2)