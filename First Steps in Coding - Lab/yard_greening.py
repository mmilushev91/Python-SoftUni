PRICE_PER_SQ_M = 7.61
DISCOUNT_PERCENT = 0.18

sq_metters = float(input())

total_price = sq_metters * PRICE_PER_SQ_M
discount = total_price * DISCOUNT_PERCENT
final_price = total_price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
