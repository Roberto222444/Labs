def sum_of_digits(n):
    if n < 10:
        return n
    else: 
        a = n % 10
        b = n // 10
        return a + sum_of_digits(b)

x = int(input("Введіть будь-яке велике ціле число: "))
result = sum_of_digits(x)

print(f"Сума цифр числа {x} дорівнює: {result}")