# # a set cannot have duplicate values
# s = {"Geeks", "for", "Geeks"}
# print("The originalset is",s)

# # values of a set cannot be changed
# s[1] = "Hello"
# print(s)

# arr= [10,5,3,4,3,5,6]
# n =len(arr)
# k =3
# flag =0
# for i in range(n):
#     if i+1+k<=n:
#         subarr =arr[i+1:i+1+k]
#         print("Sub array is ", subarr)
#         if arr[i]in subarr:
#             flag=1
#             print(f"{arr[i]}found in {subarr}",)
#     else:
#         pass
# if flag:
#     print("Duplicates Found")
# else:
#     print("No Duplicates")

arr= [10,5,3,4,3,5,6]
n =len(arr)
k =3
flag =0
for i in range(n):
    if i+1+k<=n:
        c= i+1+k
        for j in range(i+1,c):
            if arr[i]== arr[j]:
                flag =1
                print(f"{arr[i]} is duplicate ")
if flag:
    print("Duplicate found") 
else:
    print("No duplicate")   

