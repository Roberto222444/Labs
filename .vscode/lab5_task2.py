sen = input("Введіть речення: ")
if not sen[0].isupper() :
    print("Увага: Речення має починатися з великої літери!")
if not (sen.endswith(".") or sen.endswith("!") or sen.endswith("?")):
    sen = sen + "."
sen1 = sen.lower()
sen1 = sen1.replace("погано", "***")
sen1 = sen1.replace("жахливо", "***")
sen1 = sen1.replace("помилка", "***")
print(sen1)