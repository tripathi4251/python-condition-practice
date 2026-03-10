salary=int(input("enter salary:"))
if salary>=50000:
  bonus=salary*0.20
elif salary>=30000:
   bonus=salary*0.10
else:
   bonus=salary*0.05
   total_salary=salary+bonus
   print("bonus:" ,bonus)
   print("total salary:" ,total_salary)

