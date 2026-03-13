SECRET_PASSWORD = "python_super"
attempts = 3
while attempts > 0:
    user_input = input(f"Введіть пароль (залишилось спроб - {attempts}): ")
    if user_input == SECRET_PASSWORD:
        print("Доступ дозволено! Ласкаво просимо до системи.")
        break # Негайний вихід з циклу, якщо пароль вірний
    else:
        attempts -= 1 # Зменшуємо кількість спроб на 1
        print("Неправильний пароль.")
# Цей блок else відноситься до циклу while!
# Він виконається ТІЛЬКИ якщо цикл завершився природно (умова стала False),
# тобто якщо не спрацював break.
else:
    print("Систему заблоковано! Вичерпано ліміт спроб.")