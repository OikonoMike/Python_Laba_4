from src.book import Book
from src.collections import BookCollection, IndexDict

def test_book_collection():
    b1 = Book('A', 'B', 2000, 'g', '1')
    b2 = Book('C', 'D', 2001, 'h', '2')
    coll = BookCollection([b1, b2])
    assert len(coll) == 2
    assert coll[0] == b1
    assert list(coll[1:]) == [b2]
    assert list(coll) == [b1, b2]

def test_book_collection_append_remove():
    b1 = Book('A', 'B', 2000, 'g', '1')
    b2 = Book('C', 'D', 2001, 'h', '2')
    coll = BookCollection()
    coll.append_book(b1)
    coll.append_book(b2)
    assert len(coll) == 2
    coll.remove_book(b1)
    assert len(coll) == 1
    assert coll[0] == b2

def test_index_dict():
    b1 = Book('1984', 'Джордж Оруэлл', 1949, 'антиутопия', '123', 18)
    b2 = Book('О дивный...', 'Хаксли', 1932, 'антиутопия', '456', 18)
    index = IndexDict()
    index['123'] = b1
    index['456'] = b2
    assert len(index) == 2
    assert index['123'] == b1
    assert b1 in index.get_books_by_author('Джордж Оруэлл')
    assert len(index.get_books_by_year(1949)) == 1
    del index['123']
    assert '123' not in index
    assert len(index) == 1