import random , math
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+"
n = int(input("Введіть довжину: "))
num_letters = math.ceil(n * 0.5)
num_digits = math.floor(n * 0.25)
num_symbols = math.floor(n * 0.25)
letters1 = random.choices(letters , k = num_letters)
digits1 = random.choices(digits , k = num_digits)
symbols1 = random.choices(symbols , k = num_symbols)
password_chars = letters1 + digits1 + symbols1
random.shuffle(password_chars)
password1 = "".join(password_chars)
print(f"Згенерований пароль: {password1}")