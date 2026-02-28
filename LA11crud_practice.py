print("5 Names")

names = ["jhaye", "zylk", "sean", "drin", "anna", "manuel"]
print("Initial list:", names)

names.append("danna")
print("After append:", names)

names.insert(1, "hanna")
print("After insert:", names)

names[2] = "Jhaye Pelicano"
print("Updating 3rd names:", names)

names.remove("sean")
print("After remove:", names)

names.pop(-1)
print("After pop:", names)

print("Final list:", names)
print("Length of the list:", len(names))