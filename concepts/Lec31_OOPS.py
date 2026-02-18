from loguru import logger
## Calculating the total no of labours created in our class
class Labour :
    total_count =0
    def __init__(self,first_name,last_name,wage):
        self.first_name = first_name
        self.last_name = last_name
        self.wage =wage
        Labour.total_count +=1
    

Sitaram = Labour("Sitaram","Gupta",500)
print(f"Total Employees: {Labour.total_count}")
Munna = Labour("Munna","Bhai",400)
print(f"Total Employees: {Labour.total_count}")

        