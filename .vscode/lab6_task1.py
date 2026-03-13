shopping_cart = []
items_count = int(input("Скільки товарів ви хочете додати до кошика? "))
for i in range(items_count):
    item = input(f"Введіть назву товару No{i + 1}: ")
    shopping_cart.append(item.capitalize())
print("\n--- ВАШ КОШИК ---")
# Спосіб перебору елементів колекції
counter = 1
for product in shopping_cart:
    print(f"{counter}. {product}")
    counter += 1
    
print(f"Всього товарів: {len(shopping_cart)}")