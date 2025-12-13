from src.book import Book
from src.collections import BookCollection, IndexDict

class Library:
    """Класс библиотеки"""

    def __init__(self):
        self.books = BookCollection() # коллекция всех книг
        self.indexes = IndexDict() # коллекция индексов

    def add_book(self, book: Book) -> None:
        """Добавление новой книги в библиотеку"""
        self.books.append_book(book)
        self.indexes[book.isbn] = book

    def remove_book(self, isbn: str) -> None:
        """Удаление книги по ISBN"""
        if isbn not in self.indexes:
            raise KeyError(f'Книга с ISBN {isbn} не найдена')
        book_to_remove = self.indexes[isbn]
        del self.indexes[isbn]
        self.books.remove_book(book_to_remove)

    def find_by_isbn(self, isbn: str) -> Book:
        """Нахождение книг по ISBN"""
        return self.indexes[isbn]

    def find_by_author(self, author: str) -> list[Book]:
        """Нахождение книг по автору"""
        return self.indexes.get_books_by_author(author)

    def find_by_year(self, year: int) -> list[Book]:
        """Нахождение книг по году"""
        return self.indexes.get_books_by_year(year)