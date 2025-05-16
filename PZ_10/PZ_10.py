# Определим коллекции книг в разных магазинах
try:
    magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
    dom_knigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
    bukmarket = {"Пушкин", "Достоевский", "Маяковский"}
    galereya = {"Чехов", "Тютчев", "Пушкин"}

    # 1. Полный список всех книг
    all_books = magistr | dom_knigi | bukmarket | galereya
    print("Полный список всех книг:", all_books)

    # 2. Какие книги есть во всех магазинах
    common_books = magistr & dom_knigi & bukmarket & galereya
    print("Книги, которые есть во всех магазинах:", common_books)

    # 3. Хотя бы одну книгу, которая есть не во всех магазинах
    all_stores = [magistr, dom_knigi, bukmarket, galereya]

    not_in_all_stores = set()
    for store in all_stores:
        not_in_all_stores.update(store)

    # Убираем книги, которые есть во всех
    unique_books = not_in_all_stores - common_books

    print("Хотя бы одна книга, которая есть не во всех магазинах:", unique_books.pop() if unique_books else "Нет таких книг")

except ValueError:
    print("Ошибка")
