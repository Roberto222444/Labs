import sys
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n = int(input("Введіть число: "))
if n < 0 :
    print("Помилка: число має бути додатним!")
    sys.exit()
else:
    x = fibonacci(n)
    print(f"Число Фібоначчі {n} дорівнює {x}")