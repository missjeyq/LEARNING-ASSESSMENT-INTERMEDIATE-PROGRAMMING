print("\n=== String Basics ===")

name = str(input("Enter your full name:" ))

print("First character:", name[0])
print("Last character:", name[-1])

print("Enter first 5 characters:", name[:5])

print("Reversed name:", name[::-1])

print("Every other character name:", name[::2])

length = len(name)

if length % 2 == 0:
    middle = name[length//2-1:length//2+1]

else:
    middle = name[length//2]

print("Middle character:", middle)