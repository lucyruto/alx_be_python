income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
mothly_savings = income - expenses
interest = 0.05
Annual_Savings = (mothly_savings * 12) + (mothly_savings * 12 * 0.05)
print(f"Your monthly savings are ${mothly_savings}")
print(f"Projected savings after one year, with interest, is: ${Annual_Savings}")