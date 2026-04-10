students = [("Максим", 75),("Анна", 92),("Олег", 85),("Вікторія", 98)]
students.sort(key=lambda student: student[1], reverse=True)
num = 1 
for name , grade in students:
    print(f"{num} місце: {name} - {grade} балів")
    num += 1
students.sort(key=lambda student: len(student[0]))
num = 1
for name , grade in students:
    print(f"{num} {name} - {grade} балів")
    num += 1