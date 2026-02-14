## break only exits inner loop
# for i in range(3):           # OUTER LOOP
#     print(f"Outer: i={i}")
#     for j in range(3):       # INNER LOOP
#         print(f"  Inner: j={j}")
#         if j == 1:
#             break            # ← Breaks ONLY inner loop
#     print(f"Outer continues: i={i}\n")


my_dict = {'name': 'John', 'age': 30, 'city': 'Delhi'}
# keys = my_dict.keys()
# print(keys)  # dict_keys(['name', 'age', 'city'])

res_li = [key for key in my_dict]
print(res_li)