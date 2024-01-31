from datetime import datetime

DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

subtotal = 0

print("Enter the price and quantity for each item. Enter '0' for price to finish.")
price = 1

while price != 0:
    price = float(input("Please enter the price (enter '0' to finish): "))
    
    if price != 0:
        quantity = int(input("Please enter the quantity: "))
        subtotal += price * quantity
        print()

subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal:.2f}")
print()

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
    discount = round(subtotal * DISC_RATE, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount
else:
    if day_of_week == 1 or day_of_week == 2:
        lacking = max(0, 50 - subtotal)
        print(f"To receive the discount, add {lacking:.2f} to your order.")

sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax
print(f"Total: {total:.2f}")
