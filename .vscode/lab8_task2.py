students_grades = {"Марія": [85, 90, 92, 88], "Олег": [70, 75, 80, 72], "Анна": [95, 98, 100, 96]}
best_student = ""
max_avg = 0
for name, grades in students_grades.items():
    avg = sum(grades) / len(grades)
    print(f"Студент: {name}")
    print(f"Середній бал: {avg}")
    if avg > max_avg:
        max_avg = avg
        best_student = name
print (f"Найкращий студент: {best_student} , {max_avg}")