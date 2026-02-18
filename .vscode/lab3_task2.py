username_input = input("Введіть ваше ім'я (або натисніть Enter для анонімності): ")
final_name = username_input or "Anonymous"
age_input = input("Введіть вік (або натисніть Enter - за замовчуванням 18): ")
age = int(age_input or "18")
print("Профіль створено:")
print("Ім'я:", final_name)
print("Вік:", age)