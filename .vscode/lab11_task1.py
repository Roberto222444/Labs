import adv_math
import random
import sys
print("--- Гра: Вгадай НСД ---")
print("Введіть 'q' у будь-який момент для виходу з гри.")
while True:
# Генеруємо два випадкових числа від 10 до 100
    num1 = random.randint(10, 100)
    num2 = random.randint(10, 100)

    correct_gcd = adv_math.recursive_gcd(num1, num2)
    user_input = input(f"Який НСД для чисел {num1} та {num2}? Ваша відповідь: ")
# Перевірка на примусовий вихід
    if user_input.lower() == 'q':
        print("Дякуємо за гру! Завершення програми...")
        sys.exit() 
        # Негайне завершення роботи скрипта
# Конвертуємо введення у число та перевіряємо
    if int(user_input) == correct_gcd:
        print("Правильно! Ви чудово знаєте математику.")
    else:
        print(f"Помилка. Правильний НСД був: {correct_gcd}")