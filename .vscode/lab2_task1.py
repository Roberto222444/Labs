name = input("Введіть ваше ім'я:")
birth_year_str = input("Введіть рік вашого народження: ")
birth_year = int(birth_year_str)
current_year = 2026
birth_year = int(birth_year_str)
age = current_year - birth_year
print("Привіт,", name, "! Ваш вік приблизно:", age, "років.")