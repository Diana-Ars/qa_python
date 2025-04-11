import pytest

from data import *

from main import BooksCollector

@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture()
def book(collector):
    collector.add_new_book(BOOK_TITLE)
    return collector

@pytest.fixture()
def genre(book):
    book.set_book_genre(BOOK_TITLE, BOOK_GENRE)
    return book

@pytest.fixture()
def sorted_books_by_genre(collector):
    books = [
        ('Война миров', 'Фантастика'),
        ('Автостопом по галактике', 'Фантастика'),
        ('Хоббит', 'Фэнтези'),
        ('Десять негритят', 'Детектив'),
        ('Дракула', 'Ужасы')
    ]
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector
