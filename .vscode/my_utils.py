def recursive_factorial(n):
# Базовий випадок: якщо n дорівнює 1 або 0, повертаємо 1
    if n <= 1:
        return 1
# Рекурсивний крок: функція викликає сама себе
    else:
        return n * recursive_factorial(n - 1)
def greet_user(name):
    return f"Вітаємо, {name}! Це функція з власного модуля."