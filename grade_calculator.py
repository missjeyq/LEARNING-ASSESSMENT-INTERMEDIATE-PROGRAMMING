print("Grade Calculator")
user_score = int(input("Enter your score here (0-100): "))
if user_score < 0 or user_score > 100:
    print("Invalid Scores: Enter a value between 0 and 100.")

elif user_score <= 100 and user_score >= 94:
    grade = "A+"
    message = "Very Good"
    print("Score:",user_score, "Grade:",grade, "-",message)
elif user_score <= 93 and user_score >= 90:
    grade = "A-"
    message = "Nice"
    print("Score:",user_score, "Grade:",grade, "-",message)
elif user_score <= 89 and user_score >= 87:
    grade = "B+"
    message = "Good"
    print("Score:",user_score, "Grade:",grade, "-",message)
elif user_score <= 86 and user_score >= 83:
    grade = "B"
    message = "Ayos"
    print("Score:",user_score, "Grade:",grade, "-",message)
elif user_score <= 83 and user_score >= 80:
    grade = "B-"
    message = "Pede ka ha"
    print("Score:",user_score, "Grade:",grade, "-",message)
elif user_score <= 79 and user_score >= 77:
    grade = "C+"
    message = "Okay na din"
    print("Score:",user_score, "Grade:",grade, "-",message)
elif user_score <= 76 and user_score >= 73:
    grade = "C"
    message = "Solid"
    print("Score:",user_score, "Grade:",grade, "-",message)
elif user_score <= 72 and user_score >= 67:
    grade = "C-"
    message = "Ngii"
    print("Score:",user_score, "Grade:",grade, "-",message)
elif user_score <= 66 and user_score >= 60:
    grade = "D+"
    message = "Passed"
    print("Score:",user_score, "Grade:",grade, "-",message)
elif user_score <= 59:
    grade = "D"
    message = "Failed"
    print("Score:",user_score, "Grade:",grade, "-",message)
else:
    print()
    
    
#base system
#https://share.google/JqVhu0mf5SDTe5V7y
