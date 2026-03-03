email = input("Введіть ваш email: ").strip().lower()
password = input("Введіть пароль: ").strip()

if "@" not in email:
    print("Помилка: Email повинен містити символ '@'.")
elif not (email.endswith(".com") or email.endswith(".net") or email.endswith(".ua")):
    print("Помилка: Дозволені лише домени .com, .net або .ua.")
else:
    print("Email прийнято.")
    email_valid = True
    if len(password) < 8:
        print("Помилка: Пароль занадто короткий (мінімум 8 символів).")
    elif " " in password:
        print("Помилка: Пароль не повинен містити пробілів.")
    elif password.islower() or password.isupper():
        print("Помилка: Пароль має містити як великі, так і малі літери.")
    else:
        print("Пароль прийнято.") 
        at_index = email.find("@")
        username = email[:at_index]
        print(f"Реєстрація успішна! Ваш логін: {username}")