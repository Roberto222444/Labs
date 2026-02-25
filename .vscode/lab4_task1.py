raw_first_name = input("Введіть ваше ім'я: ")
raw_last_name = input("Введіть ваше прізвище: ")
first_name = raw_first_name.strip().capitalize()
last_name = raw_last_name.strip().capitalize()
if not first_name or not last_name:
   print("Помилка: Ім'я або прізвище не можуть бути порожніми!")
else:
# Використовуємо f-рядок для зручного форматування
   full_name = f"{first_name} {last_name}"
   length = len(full_name) - 1 # віднімаємо пробіл
print(f"Профіль збережено: {full_name}")
print(f"Ваше ім'я та прізвище складаються з {length} літер.")