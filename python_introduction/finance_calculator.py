monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your total monthly expenses: '))

# Calculate Monthly Savings
monthly_saving = float(monthly_income) - float(monthly_expenses)

# Project Annual Savings
# Assume a simple annual interest rate of 5%
yearly_project_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

# Output Results
print(f'Your monthly savings are ${monthly_saving:.2f}.')
print(f'Projected savings after one year, with interest, is: ${yearly_project_saving:.2f}.')