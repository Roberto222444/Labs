Num = input("Введіть номер картки: ")
Num = Num.replace(" ","")
if len(Num) != 16 or not Num.isdigit():
    print("Помилка: Неправильний формат картки.")
else:
    print (f"Ваша картка:  {Num[0:4]} **** **** {Num[12:]} ")