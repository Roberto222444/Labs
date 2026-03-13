temperatures = []
for i in range(7):
    t = float (input("Введіть температуру: "))
    temperatures.append(t)
sum_temp = 0 
count_positive = 0
count_negative = 0
for el in temperatures:
    sum_temp += el
    if el > 0:
        count_positive += 1
    else:
        count_negative += 1
x = (sum_temp/7)
print(temperatures)
print (f"Середня температура: {x}")
print  (f"Кількість днів з плюсовою температурою: {count_positive}")
print  (f"Кількість днів з мінусовою температурою: {count_negative}")