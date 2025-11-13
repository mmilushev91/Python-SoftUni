MONTHS_IN_YEAR = 12

deposited_money = float(input())
months = int(input())
annual_interest_percent = (float(input())) / 100

#calculating yearly gain
annual_interest_gain = deposited_money * annual_interest_percent

#calculating montly gain 
montly_interest_gain = annual_interest_gain / MONTHS_IN_YEAR

#calculating real gain 
interest_gain = montly_interest_gain * months

#calculating total deposit including interest
final_money = deposited_money + interest_gain

print(final_money)
