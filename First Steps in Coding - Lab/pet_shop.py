DOG_PACKAGE_PRICE = 2.5
CAT_PACKAGE_PRICE = 4

dog_packages_count = int(input())
cat_packages_count = int(input())

dog_food_price = dog_packages_count * DOG_PACKAGE_PRICE
cat_food_price = cat_packages_count * CAT_PACKAGE_PRICE


total_cost = dog_food_price + cat_food_price

print(f"{total_cost} lv.")
