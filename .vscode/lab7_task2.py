inventory = [("Телевізор", 20000, 6), ("Відеокарта", 1000, 28), ("Клавіатура", 1500, 10)]
total_value = 0
for name, price, quantity in inventory:
    x = price * quantity
    total_value += x
print(f"Товар: {name}, Загальна вартість: {x} грн")
print(f"Загальна вартість усього складу: {total_value} грн")