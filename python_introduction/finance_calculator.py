user_monthly_income = int(input('Enter your monthly income: '))
user_monthly_expenses = int(input('Enter your monthly expenses: '))

monthly_savings = user_monthly_income - user_monthly_expenses
print (f'Your monthly savings are ${monthly_savings}.')

annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05 )
print (f'Projected savings after one year, with interest, is: ${projected_savings}.')
