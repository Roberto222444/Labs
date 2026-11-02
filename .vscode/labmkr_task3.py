flights = [
    ("АН-1", 67, 348),
    ("АН-2", 93, 517),
    ("АН-1", 124, 683),
    ("АН-3", 56, 291),
    ("АН-2", 87, 462),
    ("АН-1", 105, 594),
    ("АН-3", 118, 637),
    ("АН-2", 76, 409)
]

total_time = {}
flight_count = {}

# Підрахунок нальоту та кількості польотів
for flight in flights:
    plane = flight[0]
    duration = flight[1]

    if plane not in total_time:
        total_time[plane] = 0
        flight_count[plane] = 0

    total_time[plane] += duration
    flight_count[plane] += 1

# Визначення борту з найбільшим нальотом
best_plane = max(total_time, key=total_time.get)

print("Сумарний наліт:")
print(total_time)

print("Кількість польотів:")
print(flight_count)

print("Борт з найбільшим нальотом:", best_plane)
print("Наліт:", total_time[best_plane], "хвилин")

# Обчислення середньої швидкості кожного польоту
speeds = [
    (flight[0], flight[1], flight[2],
     flight[2] / (flight[1] / 60))
    for flight in flights
]

# Сортування за спаданням швидкості
speeds.sort(key=lambda flight: flight[3], reverse=True)

# Виведення таблиці
print("\nТаблиця польотів:")
print("Борт\tТривалість\tДальність\tШвидкість")

for flight in speeds:
    print(f"{flight[0]}\t{flight[1]}\t\t{flight[2]}\t\t{flight[3]:.2f}")