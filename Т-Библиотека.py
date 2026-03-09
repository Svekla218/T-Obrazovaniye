import json
import os

FILENAME = "library.json"

def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(books):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def main():
    books = load_data()

    while True:
        print("\n1. Добавить 2. Список 3. Поиск 4. Удалить 5. Прочитано 6. Избранное 0. Выход")
        choice = input("Действие: ")

        if choice == "1":
            book = {
                "title": input("Название: "),
                "author": input("Автор: "),
                "genre": input("Жанр: "),
                "year": input("Год: "),
                "desc": input("Описание: "),
                "is_read": False,
                "is_fav": False
            }
            books.append(book)
            save_data(books)

        elif choice == "2":
            sort_key = input("Сортировать по (title/author/year): ")
            sorted_books = sorted(books, key=lambda x: x.get(sort_key, "title"))
            for i, b in enumerate(sorted_books):
                status = "[V]" if b["is_read"] else "[ ]"
                fav = "*" if b["is_fav"] else ""
                print(f"{i}. {status} {b['title']} - {b['author']} {fav}")

        elif choice == "3":
            q = input("Поиск: ").lower()
            for b in books:
                if q in b["title"].lower() or q in b["author"].lower():
                    print(f"Найдено: {b['title']} ({b['author']})")

        elif choice == "4":
            idx = int(input("Индекс для удаления: "))
            if 0 <= idx < len(books):
                books.pop(idx)
                save_data(books)

        elif choice == "5":
            idx = int(input("Индекс книги: "))
            if 0 <= idx < len(books):
                books[idx]["is_read"] = not books[idx]["is_read"]
                save_data(books)

        elif choice == "6":
            idx = int(input("Индекс книги: "))
            if 0 <= idx < len(books):
                books[idx]["is_fav"] = not books[idx]["is_fav"]
                save_data(books)

        elif choice == "0":
            break

if __name__ == "__main__":
    main()
