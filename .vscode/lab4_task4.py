Num = input("Введіть номер телефону : ")
if  Num.startswith("+38") and len(Num) == 13:
    Num = Num[3:]
Num3 = Num[0:3]
if Num3 in ["067", "096", "097", "098"]:
    print("Оператор: Київстар")
elif Num3 in ["050", "066", "095" ,"099"]:
    print("Оператор: Vodafone")
elif Num3 in ["063", "073", "093"]:
    print("Оператор: Lifecell")
else:
    print("Оператор: Невідомий")