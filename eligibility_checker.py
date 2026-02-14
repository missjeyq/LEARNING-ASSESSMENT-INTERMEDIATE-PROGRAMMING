print("Eligibility Checker")

user_age = int(input("Enter user age: "))
valid_id = input("Do you have a valid ID? yes/no: ")
has_id = valid_id == "yes"

if user_age >= 18 and has_id:
    print("Eligible")
else:
    print("Not Eligble")
if user_age >= 60:
    print("You have a Senior Discount")
