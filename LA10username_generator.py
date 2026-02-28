print("=== Username Generator ===")

full_name = input("Enter your full name: ").strip()
birth_year = input("Enter birth year: ").strip()

while len(full_name.split()) < 2:
    print("Invalid name. Enter at least first and last name.")
    full_name = input("Enter your full name: ").strip()

full_name = " ".join(full_name.split())
name_parts = full_name.split()

first_name = name_parts[0].lower()
last_name = name_parts[-1].lower()

first_part = first_name[:3]
last_part = last_name[:3]

year_part = birth_year[-2:]
username = first_part + last_part + year_part

print("\nGenerated username:", username)
