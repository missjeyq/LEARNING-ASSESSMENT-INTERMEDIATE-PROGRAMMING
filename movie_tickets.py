print("\n=== Movie Ticket System ===")

day = input("Enter days (weekends or weekdays): ")
type = input("Enter customer type (regular or student or senior): ")
time = input("Enter movie time: ")
tickets = int(input("Enter number of tickets: "))

if day == "weekdays":
    price = float(200) * tickets
    print(f"Base price: 200 * {tickets} = {price}")

else:
    price = float(300) * tickets
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

    
