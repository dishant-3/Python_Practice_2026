s = "{[()()]}"
st = []  
for c in s:
  
  	 # Push opening brackets onto the stack
    if c in '({[': 
        st.append(c)
    
    # Check for matching closing bracket
    elif c in ')}]':  
        ## Check the stack for mismatch bracket and break in case mismtach found
        if not st or (c == ')' and st[-1] != '(') or (c == '}' and st[-1] != '{') or (c == ']' and st[-1] != '['):
            print(False)  # Mismatched bracket
            break
        st.pop()  # Pop matched opening bracket

else:
    print(True if not st else False)  # Balanced if stack is empty

## For else feature of Python
# for item in iterable:
#     if condition:
#         break      # Skips else!
# else:              # Only runs if NO break occurred
#     [code here]

## Using Flag variable instead of For else loop
# class Solution:
#     def isBalanced(self, s):
#         stack = []
#         balanced = True
        
#         for ch in s:
#             if ch in "[({":
#                 stack.append(ch)
#             elif ch in "})]":
#                 if not stack or \
#                    (ch == ')' and stack[-1] != '(') or \
#                    (ch == ']' and stack[-1] != '[') or \
#                    (ch == '}' and stack[-1] != '{'):
#                     balanced = False
#                     break
#                 stack.pop()
        
#         return balanced and len(stack) == 0
 
## Using early return insted of break
class Solution:
    def isBalanced(self, s):
        stack = []
        
        for ch in s:
            if ch in "[({":
                stack.append(ch)
            elif ch in "})]":
                if not stack or \
                   (ch == ')' and stack[-1] != '(') or \
                   (ch == ']' and stack[-1] != '[') or \
                   (ch == '}' and stack[-1] != '{'):
                    return False  # Early return on mismatch
                stack.pop()
        
        return len(stack) == 0  # Empty stack = balanced ✓
