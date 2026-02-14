print("Eligibility Checker")

user_age = int(input("Enter user age: "))
valid_id = input("Do you have a valid ID? yes/no: ")
id_check = valid_id == "yes"

if user_age >= 18 and id_check:
    print("Eligible")
else:
    print("Not Eligble")
if user_age >= 60:
    print("You have a Senior Discount")
