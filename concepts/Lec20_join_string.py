state_dept_info = [{"state":"Bihar", "department":"IT"},
                   {"state":"Delhi","department":"Marketing"}]

query = """SELECT * FROM (
SELECT 
FROM employee_tbl as e
INNER JOIN department as d
ON e.emp_id =d.emp_id
) a
WHERE salary > 100000
"""
# res =''
# for ele in state_dept_info:
#     for key,value in ele.items():
        
li = ['geeks','for','geeks']
res= " ".join(li)
print(f"result is {res}")