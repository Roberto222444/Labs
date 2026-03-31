text = input("Введіть cлово: ").lower()
char_counts = {}
for char in text:
    if char not in char_counts:
        char_counts[char] = 1
    else :
        char_counts[char] += 1
print("Результат підрахунку:")
for letter , count in char_counts.items():
    print(f"Літера '{letter}' зустрічається {count} раз/и)")
