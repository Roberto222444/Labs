price_list = {"Яблуко": 15, "Хліб": 24, "Молоко": 32, "Сир": 120}
shopping_cart = ("Яблуко", "Молоко", "Кава", "Хліб")
total_cost = 0
for el in shopping_cart:
    if el in price_list:
        total_cost += price_list[el]
        print (f"Додано: {el} - {price_list[el]} грн")
    else:
        print (f"Товар: {el} не знайдено")
print (f"Фінальна сума: {total_cost}")