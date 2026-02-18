#saving with a raise
annual_salary =float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
#constants
portion_down_payment = 0.25*total_cost
current_savings = 0.0
monthly_salary = annual_salary / 12
r = 0.04
months = 0
#loop to calculate the number of months needed to save for the down payment, taking into account the semi-annual raise
while current_savings < portion_down_payment:
    current_savings += current_savings * 0.04 / 12
    current_savings += monthly_salary * portion_saved
    months += 1
#check if it's time for the semi-annual raise
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
#output the number of months needed to save for the down payment
print("Number of months:", months)