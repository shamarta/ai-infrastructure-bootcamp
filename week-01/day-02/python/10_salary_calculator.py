base_salary = int(input("enter your salary :"))
overtime_hours = int(input("enter your overtime hours :"))
overtime_rate = int(input("enter your overtime rate :"))

overtime_pay = (overtime_hours * overtime_rate)
final_salary = (base_salary + overtime_pay)

print(f"your final salary with overtime pay  is : {final_salary} ")
