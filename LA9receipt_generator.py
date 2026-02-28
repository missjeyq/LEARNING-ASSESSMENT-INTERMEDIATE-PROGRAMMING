print("Receipt Generator")

item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

total = quantity*unit_price

print("\n=== Receipt ===")

print(f"{"Item":15}{"Quantity":>5}{"Price":>15}")
print("-" * 35)

print(f"{item_name:15} {quantity:>5} {unit_price:>15,.2f}")
print("-" * 35)

print(f"{"Total:":>20} ₱{total:,.2f}")

print("=" * 35)