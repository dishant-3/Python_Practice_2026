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