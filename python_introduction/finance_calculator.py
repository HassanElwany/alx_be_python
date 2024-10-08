monthly_income = input('Enter your monthly income: ')
monthly_expenses = input('Enter your total monthly expenses: ')

# Calculate Monthly Savings
monthly_savings = float(monthly_income) - float(monthly_expenses)

# Project Annual Savings
# Assume a simple annual interest rate of 5%
yearly_project_saving = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output Results
print(f'Your monthly savings are ${monthly_savings:.0f}.')
print(f'Projected savings after one year, with interest, is: ${yearly_project_saving:.0f}.')