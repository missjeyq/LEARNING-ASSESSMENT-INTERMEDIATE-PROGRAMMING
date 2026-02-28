print("===Grade Calculator===")

score = float(input("Enter your score here (0-100): "))
if score < 0 or score > 100:
    print("Invalid Scores: Enter a value between 0 and 100.")

elif score <= 100 and score >= 94:
    grade = "A+"
    message = "Excellent"
elif score <= 93 and score >= 90:
    grade = "A-"
    message = "Amazing"
elif score <= 89 and score >= 87:
    grade = "B+"
    message = "Awesome"
elif score <= 86 and score >= 83:
    grade = "B"
    message = "Very Good"
elif score <= 82 and score >= 80:
    grade = "B-"
    message = "Nice"
elif score <= 79 and score >= 77:
    grade = "C+"
    message = "Good"
elif score <= 76 and score >= 73:
    grade = "C"
    message = "Passed"
elif score <= 72 and score >= 70:
    grade = "C-"
    message = "Passed"
elif score <= 69 and score >= 67:
    grade = "D+"
    message = "Passed"
elif score <= 66 and score >= 60:
    grade = "D"
    message = "Passed"
elif score <= 59:
    grade = "F"
    message = "Failed"
else:
    print()
print("Score:",score, "Grade:",grade, "-",message)

#base system
#https://share.google/1NtXqNPL0ikgmxxH8
