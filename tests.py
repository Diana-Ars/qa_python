import pytest

from data import *

class TestBooksCollector:

    @pytest.mark.parametrize(
        'name',
        [
            ('Я'),                        #1 символ;
            ('Я' * 15),                   #15 символов;
            ('Я' * 40),                   #40 символов;
    ])

    def test_add_new_book_name_length_less_than_41_symbols_and_over_0(self, collector, name):
        collector.add_new_book(name)
        assert collector.books_genre == {name:''}

    @pytest.mark.parametrize(
        'name',
    [
        ('Я' * 41),  # 41 символ;
        ('Я' * 42)   # 42 символа
    ])

    def test_add_new_book_name_length_over_than_40_symbols(self, collector, name):
        collector.add_new_book(name)
        assert collector.books_genre == {}

    def test_add_new_book_name_is_empty(self, collector):
        collector.add_new_book('')
        assert '' not in collector.books_genre

    def test_add_new_book_add_an_added_book(self, collector):
        collector.add_new_book(BOOK_TITLE)
        book_count = len(collector.books_genre)
        collector.add_new_book(BOOK_TITLE)
        assert book_count == 1

    @pytest.mark.parametrize(
        'name, genre',
        [
            (BOOK_TITLE, 'Фантастика'),
            (BOOK_TITLE, 'Ужасы'),
            (BOOK_TITLE, 'Детективы'),
            (BOOK_TITLE, 'Мультфильмы'),
            (BOOK_TITLE, 'Комедии')
        ]
    )

    def test_set_book_genre_set_genre_to_added_book(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_set_book_genre_set_existent_genre_to_added_book(self, book):
        book.set_book_genre(BOOK_TITLE, 'Фэнтези')
        assert book.get_books_genre() == {BOOK_TITLE: ''}

    def test_set_book_genre_set_genre_to_existent_book(self, collector):
        collector.set_book_genre('Хоббит', 'Мультфильм')
        assert collector.get_books_genre() == {}

    def test_get_book_genre_added_book(self, genre):
        result = genre.get_book_genre(BOOK_TITLE)
        assert result == BOOK_GENRE

    def test_get_book_genre_not_added_book(self, collector):
        result = collector.get_book_genre('Поселок')
        assert  result == None

    def test_get_books_with_specific_genre_set_genre_to_added_book(self, collector, sorted_books_by_genre):
        books_with_specific_genre = collector.get_books_with_specific_genre('Фантастика')
        assert books_with_specific_genre == [
            'Война миров',
            'Автостопом по галактике'
        ]

    def test_get_books_with_specific_genre_not_available_genre(self, collector, sorted_books_by_genre):
        books_with_specific_genre = collector.get_books_with_specific_genre('Фэнтези')
        assert books_with_specific_genre == []

    def test_get_books_genre_add_book_and_set_genre(self, genre):
        result = genre.get_books_genre()
        assert result == {BOOK_TITLE:BOOK_GENRE}

    def test_get_books_genre_empty_value(self, collector):
        result = collector.get_books_genre()
        assert result == {}

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Книга1', 'Фантастика'),
            ('Книга2', 'Мультфильмы'),
            ('Книга3', 'Комедии')
        ]
    )

    def test_get_books_for_children_by_not_genre_age_rating(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        books_for_children = collector.get_books_for_children()
        assert books_for_children == [name]

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Книга1', 'Ужасы'),
            ('Книга2', 'Детективы')
        ]
    )

    def test_get_books_for_children_by_genre_age_rating(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        books_for_children = collector.get_books_for_children()
        assert books_for_children == []

    def test_add_book_in_favorites_add_book_from_book_genre(self, book):
        book.add_book_in_favorites(BOOK_TITLE)
        favorites = book.get_list_of_favorites_books()
        assert favorites == [BOOK_TITLE]

    def test_add_book_in_favorites_add_added_book(self, book):
        book.add_book_in_favorites(BOOK_TITLE)
        book.add_book_in_favorites(BOOK_TITLE)
        favorites = book.get_list_of_favorites_books()
        book_count_favorites = len(favorites)
        assert book_count_favorites == 1

    def test_delete_book_from_favorites_added_book_in_favorites(self, book):
        book.add_book_in_favorites(BOOK_TITLE)
        book.delete_book_from_favorites(BOOK_TITLE)
        favorites = book.get_list_of_favorites_books()
        book_count_favorites = len(favorites)
        assert book_count_favorites == 0

    def test_get_list_of_favorites_books_add_book(self, book):
        book.add_book_in_favorites(BOOK_TITLE)
        result = book.get_list_of_favorites_books()
        assert result == [BOOK_TITLE]

    def test_get_list_of_favorites_books_empty_value(self, collector):
        result = collector.get_list_of_favorites_books()
        assert result == []

