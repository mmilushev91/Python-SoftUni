NYLON_PRICE_SQ_M = 1.50
PAINT_PRICE_LITTER = 14.50 
PAINT_THINNER_PRICE = 5 
ADDITIONAL_PAINT_PERCENT = 0.1
ADDITINAL_NYLON_SQ_M = 2
BAGS_PRICE = 0.40
HOURLY_WORK_PRICE_PERCENT = 0.30

nylon_sq_m = int(input())
paint_litters = int(input())
paint_thinner_litters = int(input())
work_hours = int(input())

#calculate nylon price
nylon_price = (nylon_sq_m + ADDITINAL_NYLON_SQ_M) * NYLON_PRICE_SQ_M

#calculate paint price
additional_paint = paint_litters * ADDITIONAL_PAINT_PERCENT
paint_price = (paint_litters + additional_paint) * PAINT_PRICE_LITTER

#calculate paint thinner price
paint_thinner_price = paint_thinner_litters * PAINT_THINNER_PRICE

#calculate materials price 
materials_price = nylon_price + paint_price + paint_thinner_price + BAGS_PRICE

#calculate work per hour price
work_per_hour_price = materials_price * HOURLY_WORK_PRICE_PERCENT

#calculate total work price 
total_work_price = work_per_hour_price * work_hours

#calculate final price 
final_price = materials_price + total_work_price

print(final_price)
