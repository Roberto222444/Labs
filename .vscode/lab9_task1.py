def calculate_total(price, quantity, discount=0):
# Локальна змінна (існує тільки всередині функції)
    total = price * quantity
    final_price = total - discount
# Повертаємо результат у те місце, звідки була викликана функція
    return final_price
order1 = calculate_total(500, 2)
print(f"Замовлення 1 (без знижки): {order1} грн")
order2 = calculate_total(500, 2, 150)
print(f"Замовлення 2 (зі знижкою 150): {order2} грн")
order3 = calculate_total(quantity=3, discount=50, price=200)
print(f"Замовлення 3 (іменовані параметри): {order3} грн")