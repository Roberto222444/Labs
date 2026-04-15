import sys , math , random
x = math.comb(42, 6)
print(f"Шанс виграти джекпот становить 1 до {x}")
winning_numbers = random.sample(range(1,43), 6)
winning_numbers.sort()
a = input("Введіть 6 чисел: ").strip().split()
if len(a) != 6 :
    sys.exit("Помилка: потрібно ввести рівно 6 чисел.")
a = [int(x) for x in a]
print(f"Виграшна комбінація {winning_numbers}")
b = len([x for x in a if x in winning_numbers])
print(f"Ви вгадали {b} чисел!")