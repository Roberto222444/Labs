x = 0
y = 0

commands = input("Введіть команди через кому: ").split(",")

counts = {
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0
}

for i in range(len(commands)):
    command = commands[i].strip()

    if command == "up":
        y += 1
        counts["up"] += 1

    elif command == "down":
        y -= 1
        counts["down"] += 1

    elif command == "left":
        x -= 1
        counts["left"] += 1

    elif command == "right":
        x += 1
        counts["right"] += 1

    else:
        print("Невідома команда №", i + 1)
        continue

print("Кількість команд:")
for command in counts:
    print(command, ":", counts[command])

distance = (x**2 + y**2)**0.5

print("Кінцеві координати:", (x, y))
print(f"Відстань від початку координат: {distance:.2f}")