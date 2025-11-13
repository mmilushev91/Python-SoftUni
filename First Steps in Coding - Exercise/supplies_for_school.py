PENS_PACKAGE_PRICE = 5.80
MARKERS_PACKAGE_PRICE = 7.20 
DETERGENT_LITTER_PRICE = 1.20

pens_packages_count = int(input())
markers_packages_count = int(input())
detergent_litters_count = int(input())
discount_percent = int(input()) / 100

#calculate pens price
pens_price = pens_packages_count * PENS_PACKAGE_PRICE

#calculate markers price
markers_price = markers_packages_count * MARKERS_PACKAGE_PRICE

#calculate detergent price
detergent_price = detergent_litters_count * DETERGENT_LITTER_PRICE

#calculate total price 
total_price = pens_price + markers_price + detergent_price

#calculate discount
discount = total_price * discount_percent

#calculate final price
final_price = total_price - discount

print(final_price)
