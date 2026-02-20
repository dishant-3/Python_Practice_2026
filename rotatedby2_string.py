def isRotated(s1,s2):
        n = len(s1)
        right_rotated=[0]*n
        for i in range(n):
            new_idx = (i+2)%n
            right_rotated[new_idx] = s1[i]
        
        left_rotated=[0]*n    
        for j in range(n):
            new_idx =(j-2+n)%n
            left_rotated[new_idx] = s1[j]   
        
        right_str = "".join(right_rotated)
        left_str = "".join(left_rotated)
        
        if s2 == right_str or s2 ==left_str:
            return True
        else:
            return False
s1 = "amazon"
s2 = "azonam"
print(f"Inputs:{s1},{s2}\n Output:{isRotated(s1,s2)}")
s1 = "geeksforgeeks" 
s2 = "geeksgeeksfor"
print(f"Inputs:{s1},{s2}\n Output:{isRotated(s1,s2)}")
s1 = "ab"
s2 = "ab"
print(f"Inputs:{s1},{s2}\n Output:{isRotated(s1,s2)}")