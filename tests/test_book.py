from src.book import Book, PhysicalBook, DigitalBook

def test_book_creation():
    book = Book('1984', 'Оруэлл', 1949, 'антиутопия', '978-0-123456', 18)
    assert book.title == '1984'
    assert book.age_rating == 18

def test_book_eq():
    b1 = Book('A', 'B', 2000, 'g', '123', 0)
    b2 = Book('X', 'Y', 2001, 'h', '123', 0)
    assert b1 == b2

def test_physical_book_borrow():
    pb = PhysicalBook('Война и мир', 'Лев Толстой', 1869, 'роман', '978-1', copies=2, age_rating=0)
    assert pb.is_available() is True
    pb.borrow()
    assert pb.copies_available == 1
    pb.borrow()
    assert pb.copies_available == 0
    assert pb.is_available() is False

def test_physical_book_borrow_error():
    pb = PhysicalBook('Книга', 'Автор', 2000, 'жанр', '978-2', copies=1)
    pb.borrow()
    try:
        pb.borrow()
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == 'Книги нет в наличии'

def test_digital_book():
    db = DigitalBook('Гарри Поттер', 'Роулинг', 1997, 'фэнтези', '978-3', 'EPUB', 12)
    assert db.is_available() is True
    assert db.requires_device() is True