total_seconds = int(input("Введіть кількість секунд: "))
days = total_seconds // 86400
remaining_seconds = total_seconds % 86400
hours = remaining_seconds // 3600
remaining_seconds = remaining_seconds % 3600 # оновлюємо залишок
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print("Результат конвертації (D:H:M:S):")
print(days, hours, minutes, seconds, sep=" : ")