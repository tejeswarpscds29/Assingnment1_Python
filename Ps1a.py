#House Hunting
#input: annual salary, portion saved, total cost of dream home
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))#For example, if you want to save 10%, enter 0.1
total_cost = float(input("Enter the cost of your dream home: "))
#constants
portion_down_payment = 0.25
current_savings = 0.0
#calculations
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment
months = 0
#loop to calculate the number of months needed to save for the down payment
while current_savings < down_payment:
    current_savings += current_savings * 0.04 / 12#add monthly interest to current savings
    current_savings += monthly_salary * portion_saved
    months += 1
    #output the number of months needed to save for the down payment
print("Number of months:", months)