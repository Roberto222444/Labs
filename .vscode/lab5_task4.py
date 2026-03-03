text = input("Введіть текст або слово: ").lower().replace(" ","")
reversed_text = text[::-1]
if reversed_text == text :
    print(f"Паліндром: {text}")
else:
    print(f"Не паліндром: {text}")