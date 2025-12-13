class Book:
    """Книга в списке (библиотеке)"""

    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", {self.year}, "{self.genre}", "{self.isbn}")'

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

    def __hash__(self):
        return hash(self.isbn)