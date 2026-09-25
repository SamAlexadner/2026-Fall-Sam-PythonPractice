while (monthly_investment := float(input("Enter a monthly investment amount: ")))< 0:  # check the input correct or not
    print("Error: investent must be a positive number")
while (yearly_interest_rate := float(input("Enter a yearly interest rate: ")))< 0:
    print("Error: yearly interest rate must be a positive number")
while (investment_years := int(input("Enter how many years to invest: ")))< 0:
    print("Error: investment period must be a positive number of years")

ONE_YEAR_MONTH = 12 
total_month = investment_years * ONE_YEAR_MONTH  # Calculate the total number of months
new_money = 0
monthly_interest_rate = (yearly_interest_rate / 100) / ONE_YEAR_MONTH
for month in range(1, total_month + 1):
    new_money = (monthly_investment + new_money) * (1 + monthly_interest_rate)
    print(f"Month {month} revenue: {new_money}")

total_investment = monthly_investment * total_month
total_revenue = new_money 
print(f"After {investment_years} years, you will receive a total investment revenue of {total_revenue:,.2f} at a yearly rate of {yearly_interest_rate:.1f}")
