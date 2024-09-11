monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

# Calculate Monthly Savings
monthly_saving = monthly_income - monthly_expenses

# Project Annual Savings
# Assume a simple annual interest rate of 5%
yearly_project_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

# Output Results
print(f'Your monthly savings are ${monthly_saving}.')
print(f'Projected savings after one year, with interest, is: ${yearly_project_saving}.')