print("2D List")

gradebook = [
    ["Sean", 45, 48, 50],
    ["Zylk", 49, 38, 42],
    ["Jhaye", 50, 50, 50],
    ["Drin", 38, 27, 29]
]

for row in gradebook:
    print(row)

print("=============")

print("2nd student quiz2 score:", gradebook[1][2])

gradebook[2][1] = 100

gradebook.append(["Hanna", 42, 44, 38])

for row in gradebook:
    print(row)
