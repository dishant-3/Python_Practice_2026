## Brute force approach
# def ispalindrome(str):
#     n = len(str)
#     rev = []
#     for i in range(n-1,-1,-1):
#         rev.append(str[i])
#     rev_str =''.join(rev)
#     # print(f"Input:{str}\n Reverse string is:{rev_str}")    
#     if rev_str == str:
#         return True
#     else:
#         return False

def ispalindrome(str):
    n = len(str)
    right = n-1
    left = 0
    while left <right:
        if str[left] != str[right]:
            return False
        else:
            left = left +1
            right = right -1
            
    return True
res1 = ispalindrome("level")
print(res1)
res2 = ispalindrome("amma")
print(res2)
res3 = ispalindrome("dishant")
print(res3)