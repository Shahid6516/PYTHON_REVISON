score = int(input("Your score is : "))

if score > 100:
    grade = "Wrong Score"
elif score >= 90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade )