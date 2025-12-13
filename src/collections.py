from typing import Union, Iterator
from src.book import Book

class BookCollection:
    """Списковая коллекция книг (через композицию)"""

    def __init__(self, books: list[Book] | None = None):
        self._books = books or []

    def __getitem__(self, key: Union[int, slice]) -> Union[Book, 'BookCollection']:
        if isinstance(key, slice):
            return BookCollection(self._books[key])
        return self._books[key]

    def __iter__(self) -> Iterator[Book]:
        return iter(self._books)

    def __len__(self) -> int:
        return len(self._books)


    # методы добавления и удаления книг:
    def append_book(self, book: Book) -> None:
        """Метод добавления книги"""
        self._books.append(book)

    def remove_book(self, book: Book) -> None:
        """Метод удаления книги"""
        self._books.remove(book)

    def pop(self, index: int = -1) -> Book:
        """Метод удаления книги по индексу"""
        return self._books.pop(index)


class IndexDict:
    """Пользовательская словарная коллекция с индексацией по ISBN, автору, году"""

    def __init__(self):
        self._data = {}
        self._by_author = {}
        self._by_year = {}

    def _update_indexes(self, book: Book) -> None:
        # ISBN
        self._data[book.isbn] = book

        # Автор
        if book.author not in self._by_author:
            self._by_author[book.author] = []
        if book not in self._by_author[book.author]:
            self._by_author[book.author].append(book)

        # Год
        if book.year not in self._by_year:
            self._by_year[book.year] = []
        if book not in self._by_year[book.year]:
            self._by_year[book.year].append(book)

    def __setitem__(self, isbn: str, book: Book) -> None:
        if isbn != book.isbn:
            raise ValueError('ISBN в ключе и книге должны совпадать')
        self._update_indexes(book)

    def __getitem__(self, isbn: str) -> Book:
        return self._data[isbn]

    def __delitem__(self, isbn: str) -> None:
        book = self._data.pop(isbn)
        # Удалить из индексов
        self._by_author[book.author].remove(book)
        if not self._by_author[book.author]:
            del self._by_author[book.author]
        self._by_year[book.year].remove(book)
        if not self._by_year[book.year]:
            del self._by_year[book.year]

    def __contains__(self, isbn: str) -> bool:
        return isbn in self._data

    def __len__(self) -> int:
        return len(self._data)

    def get_books_by_author(self, author: str) -> list[Book]:
        return self._by_author.get(author, [])

    def get_books_by_year(self, year: int) -> list[Book]:
        return self._by_year.get(year, [])