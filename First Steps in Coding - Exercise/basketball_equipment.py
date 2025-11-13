annual_tax = int(input())

basketball_shoes = annual_tax - annual_tax * 0.40
basketball_outfit = basketball_shoes - basketball_shoes * 0.20
basketball = basketball_outfit / 4 
basketball_accessories = basketball / 5

total_price = basketball_shoes + basketball_outfit + basketball + \
    basketball_accessories + annual_tax

print(total_price)
