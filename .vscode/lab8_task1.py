library_catalog = {
    "Фантастика": [],
    "Детектив": [],
    "Історія": []
}
library_catalog["Фантастика"].append(("Дюна", "Френк Герберт"))
library_catalog["Фантастика"].append(("1984", "Джордж Оруелл"))
library_catalog["Детектив"].append(("Пригоди Шерлока Холмса", "Артур Конан Дойл"))
library_catalog["Наука"] = [("Коротка історія часу", "Стівен Гокінг")]
print("--- КАТАЛОГ БІБЛІОТЕКИ ---")
for genre, books_list in library_catalog.items():
    print(f"Жанр: {genre}")
    
    if not books_list:
        print("  Книг поки немає.")
        continue
        

    for title, author in books_list:
        print(f"  '{title}' (Автор: {author})")