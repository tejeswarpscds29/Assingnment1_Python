#Finding the right amount to save away each month to make a down payment on a dream home
annual_salary = float(input("Enter the starting salary: "))
#Assumptions
total_cost = 1000000
semi_annual_raise = 0.07
annual_return = 0.04
portion_down_payment = 0.25 * total_cost
monthly_return = annual_return / 12
months = 36
# Bisection search setup
low = 0
high = 10000
steps = 0
best_rate = 0
# Check if it is possible even with 100% saving rate
current_savings = 0
current_salary = annual_salary
# Simulate savings for 36 months with 100% saving rate
for i in range(months):
    current_savings += current_savings * monthly_return
    current_savings += (current_salary / 12)
    if (i + 1) % 6 == 0:
        current_salary += current_salary * semi_annual_raise
# If even with 100% saving rate we can't afford the down payment, print that it's not possible
if current_savings < portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
# Otherwise, perform bisection search to find the best saving rate
else:
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        rate = mid / 10000
# Simulate savings for 36 months with the current saving rate
        current_savings = 0
        current_salary = annual_salary
#loop to calculate the savings after 36 months with the current saving rate   
        for i in range(months):
            current_savings += current_savings * monthly_return
            current_savings += (current_salary / 12) * rate
#check if it's time for the semi-annual raise
            if (i + 1) % 6 == 0:
                current_salary += current_salary * semi_annual_raise
 #check if the current savings is within $100 of the required down payment
        if abs(current_savings - portion_down_payment) <= 100:
            best_rate = rate
            break
        elif current_savings < portion_down_payment:
            low = mid + 1
        else:
            high = mid - 1
    
    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)
    #output the best saving rate and the number of steps in the bisection search
