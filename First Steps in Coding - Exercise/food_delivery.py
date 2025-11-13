CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DESERT_PERCENT = 0.2
DELIVERY_PRICE = 2.5

chicken_menus_count = int(input())
fish_menus_count = int(input())
vegetarian_menus_count = int(input())

#calculate chicken price
chicken_price = chicken_menus_count * CHICKEN_MENU_PRICE

#calculate fish price
fish_price = fish_menus_count * FISH_MENU_PRICE

#calculate vegetarian price
vegetarian_price = vegetarian_menus_count * VEGETARIAN_MENU_PRICE

#calculate menus price
menus_price = chicken_price + fish_price + vegetarian_price

#calculate desert price
desert_price = menus_price * DESERT_PERCENT

#calculate total price
total_price = menus_price + desert_price + DELIVERY_PRICE

print(total_price)
