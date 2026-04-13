import my_utils
import math
import sys
print(my_utils.greet_user("Студент"))
number = 5
# Виклик нашої рекурсивної функції
my_result = my_utils.recursive_factorial(number)
# Виклик вбудованої функції з модуля math
math_result = math.factorial(number)
print(f"Факторіал {number} (наша рекурсія): {my_result}")
print(f"Факторіал {number} (модуль math): {math_result}")
print("\n--- Системна інформація ---")
print(f"Платформа: {sys.platform}")
print(f"Версія Python: {sys.version.split()[0]}")