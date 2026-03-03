link = input("Введіть URl: ")
index = link.find("://")
if index == -1:
    print("Помилка: Неправильний формат посилання")
else:
    pro = link[:index]
    if pro == "https" :
        print("З'єднання безпечне")
    else :
        print("З'єднання небезпечне")
dom = link[index+3:]
print(f"Протокол: {pro}")
print(f"Домен: {dom}")