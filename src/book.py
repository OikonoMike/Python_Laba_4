class Book:
    """Книга в списке (библиотеке)"""

    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, age_rating: int = 0):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
        self.age_rating = age_rating

    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", {self.year}, "{self.genre}", "{self.isbn}")'

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

    def __hash__(self):
        return hash(self.isbn)



class PhysicalBook(Book):
    """Физическая книга (имеет ограниченное количество экземпляров)"""

    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, copies: int = 1, age_rating: int = 0):
        super().__init__(title, author, year, genre, isbn, age_rating)
        self.copies_total = copies
        self.copies_available = copies

    def is_available(self) -> bool:
        """Проверить, есть ли свободные экземпляры"""
        return self.copies_available > 0

    def borrow(self) -> bool:
        """Взять книгу (уменьшить доступное количество)"""
        if self.is_available():
            self.copies_available -= 1
            return True
        return False

    def return_copy(self) -> None:
        """Вернуть книгу (увеличить доступное количество)"""
        if self.copies_available < self.copies_total:
            self.copies_available += 1



class DigitalBook(Book):
    """Электронная книга (всегда доступна, имеет формат файла)"""

    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, file_format: str = "PDF", age_rating: int = 0):
        super().__init__(title, author, year, genre, isbn, age_rating)
        self.file_format = file_format

    def is_available(self) -> bool:
        """Электронная книга всегда доступна"""
        return True

    def requires_device(self) -> bool:
        """Требуется устройство для чтения"""
        return True