import random
from src.Library import Library
from src.book import PhysicalBook, DigitalBook

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """
    Симуляция работы библиотеки.
    На каждом шаге происходит одно случайное событие.
    """
    print('Вы запустили симуляцию библиотеки...')
    print('Симуляция состоит из 10 произвольных событий:')
    if seed is not None:
        random.seed(seed)

    # Известные книги
    TITLES = [
        'Война и мир',
        'Преступление и наказание',
        '1984',
        'Мастер и Маргарита',
        'Гарри Поттер и философский камень',
        'Анна Каренина',
        'Граф Монте-Кристо',
        'О дивный новый мир',
        'Три товарища',
        'Маленький принц'
    ]
    # Известные авторы
    AUTHORS = [
        'Лев Толстой',
        'Фёдор Достоевский',
        'Джордж Оруэлл',
        'Михаил Булгаков',
        'Дж. К. Роулинг',
        'Александр Дюма',
        'Алдус Хаксли',
        'Эрих Мария Ремарк',
        'Антуан де Сент-Экзюпери'
    ]
    # Популярные жанры
    GENRES = ['роман', 'антиутопия', 'фэнтези', 'классика']

    # Создаём библиотеку
    library = Library()

    for step in range(1, steps + 1):
        event = random.choice([
            'add_book',
            'remove_book',
            'search_by_author',
            'search_by_year',
            'search_invalid_isbn',
            'borrow_physical_book'
        ])

        if event == 'add_book':
            # Генерируем случайную книгу и добавляем в библиотеку
            title = random.choice(TITLES)
            author = random.choice(AUTHORS)
            year = random.randint(1800, 2024)
            genre = random.choice(GENRES)
            isbn = f'999-{random.randint(100000000, 999999999)}'
            age_rating = (18 if title in ['1984', 'О дивный новый мир'] else 0)

            if random.choice([True, False]):
                # Физическая книга
                copies = random.randint(1, 5)
                book = PhysicalBook(title, author, year, genre, isbn, copies, age_rating)
            else:
                # Электронная книга
                format = random.choice(['PDF', 'EPUB'])
                book = DigitalBook(title, author, year, genre, isbn, format, age_rating)

            library.add_book(book)
            book_type = 'Physical' if isinstance(book, PhysicalBook) else 'Digital'
            print(f'[{step}] Добавлена книга: "{book.title}" ({book.author}, {book.year}, {book_type})')

        elif event == 'remove_book' and len(library.books) > 0:
            # Удаляем случайную книгу из библиотеки
            if len(library.books) > 0:
                book_list = library.books._books
                book_to_remove = random.choice(book_list)
                isbn_to_remove = book_to_remove.isbn
                library.remove_book(isbn_to_remove)
                print(f'[{step}] Удалена книга: "{book_to_remove.title}"')
            else:
                print(f'[{step}] Попытка удалить книгу — библиотека пуста')

        elif event == 'search_by_author':
            # Поиск книг по случайному автору
            author = random.choice(AUTHORS)
            found = library.find_by_author(author)
            print(f'[{step}] Поиск по автору "{author}": найдено {len(found)} книг')

        elif event == 'search_by_year':
            # Поиск книг по случайному году
            year = random.randint(1800, 2024)
            found = library.find_by_year(year)
            print(f'[{step}] Поиск по {year} году: найдено {len(found)} книг')

        elif event == 'search_invalid_isbn':
            # Обработка ошибки - поиск несуществующей книги
            fake_isbn = f'000-{random.randint(100000000, 999999999)}'
            try:
                library.find_by_isbn(fake_isbn)
                print(f'[{step}] Ошибка: книга с ISBN {fake_isbn} найдена (но не должна быть)')
            except KeyError:
                print(f'[{step}] Попытка найти несуществующую книгу с ISBN {fake_isbn} — не найдена')


        elif event == 'borrow_physical_book':
            if len(library.books) > 0:
                physical_books = [b for b in library.books._books if isinstance(b, PhysicalBook)]
                if not physical_books:
                    print(f'[{step}] Нет физических книг для выдачи')
                else:
                    book = random.choice(physical_books)
                    if book.is_available():
                        book.borrow()
                        print(f'[{step}] Взята книга: "{book.title}" (осталось копий: {book.copies_available})')
                    else:
                        print(f'[{step}] Попытка взять книгу "{book.title}" — все копии заняты')
            else:
                print(f'[{step}] Попытка взять книгу — библиотека пуста')
    print('Симуляция завершена.')


if __name__ == "__main__":
    run_simulation(steps=10, seed=42)