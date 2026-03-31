subjects = ("Математика", "Програмування", "Філософія")
grades = []
student_profile = {
"name": "Олександр",
"age": 19,
"group": "КН-21",
"enrolled_subjects": subjects,
"current_grades": grades
}
student_profile["current_grades"].append(95)
student_profile["current_grades"].append(88)
student_profile["current_grades"].append(92)
student_profile["has_scholarship"] = True
print("--- ПРОФІЛЬ СТУДЕНТА ---")
for key, value in student_profile.items():
    print(f"{key}: {value}")
