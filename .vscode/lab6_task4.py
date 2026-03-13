hidden_number = 42
attempts = 0 
while True: 
    guess = int(input("Вгадайте число: "))
    attempts += 1
    if guess > hidden_number:
        print("Моє число МЕНШЕ. Спробуй ще.")
    elif guess < hidden_number:
        print("Моє число БІЛЬШЕ. Спробуй ще.")
    else:
         print("Вітаю! Ти вгадав число!")
         print(f"Тобі знадобилося {attempts} спроб!")
         break
    