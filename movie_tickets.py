print("\n=== Movie Ticket System ===")

day = input("Enter days (weekends or weekdays): ")
type = input("Enter customer type (regular or student or senior): ")
time = input("Enter movie time: ")
tickets = input("Enter number of tickets: ")

if day == "weekdays":
    price = 200 * tickets
    print(f"Base price: 200 * {tickets} = {price}")

else:
    price = 300 * tickets
    print(f"Base price: 300 * {tickets} = {price}")

    if type == "student":
        discount = 0.20
        discounted_price = price * discount
        price = price - discounted_price
        print(f"Student discount (20%): {discounted_price}")

    elif type == "senior":
        discount = 0.30
        discounted_price = price * discount
        price = price - discounted_price
        print(f"Senior discount (30%): {discounted_price}")

if time < 12:
    discount = 0.10
    discounted_price = price * discount
    price = price - discounted_price
    print(f"Matinee discount (10%): {discounted_price}")

if tickets > 5:
    discount = 0.05
    discounted_price = price * discount
    price = price - discounted_price
    print(f"Group discount (5%): {discounted_price}")   

print(f"\nTOTAL: {price:.2f}")
print("Thank you for you purchased!")