from src.Library import Library
from src.book import PhysicalBook, DigitalBook

def test_library_add_remove():
    lib = Library()
    book = PhysicalBook('Война и мир', 'Лев Толстой', 1869, 'роман', '978-1', copies=1)
    lib.add_book(book)
    assert len(lib.books) == 1
    assert len(lib.indexes) == 1
    lib.remove_book('978-1')
    assert len(lib.books) == 0
    assert len(lib.indexes) == 0

def test_library_find_by_author():
    lib = Library()
    b1 = DigitalBook('1984', 'Джордж Оруэлл', 1949, 'антиутопия', '123')
    b2 = DigitalBook('Скотный двор', 'Джордж Оруэлл', 1945, 'антиутопия', '124')
    lib.add_book(b1)
    lib.add_book(b2)
    found = lib.find_by_author('Джордж Оруэлл')
    assert len(found) == 2

def test_library_remove_nonexistent():
    lib = Library()
    try:
        lib.remove_book('999-999')
        assert False, "Expected KeyError"
    except KeyError as e:
        assert 'Книга с ISBN 999-999 не найдена' in str(e)