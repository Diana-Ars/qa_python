Тестирование приложения BooksCollector

BooksCollector позволяет установить жанр книг и добавить их в избранное.

Изначально представлены: список genre, который содержит доступные жанры, и список genre_age_rating, который содержит жанры с возрастным рейтингом.


1. Тесты для метода 'add_new_book' :

	1) test_add_new_book_name_length_less_than_41_symbols_and_over_0 
	- проверка добавления книги с названием длиной более 0 и менее 41 символа 
	
	2) test_add_new_book_name_length_over_than_40_symbols
	- проверка недобавления книги с названием длиной более 40 символов 
	
	3) test_add_new_book_name_is_empty
	- проверка недобавления книги с названием "" (0 символов) 
	
	4) test_add_new_book_add_an_added_book
	- проверка недобавления дубликата книги 

2. Тесты для метода 'set_book_genre':
	
	1) test_set_book_genre_set_genre_to_added_book
	- проверка установки жанра из списка genre к добавленной книге 
	
	2) test_set_book_genre_set_existent_genre_to_added_book
	- проверка неустановки жанра не из списка genre к добавленной книге 
	
	3) test_set_book_genre_set_genre_to_existent_book
	- проверка неустановки жанра из списка genre к несуществующей книге 

3. Тесты для метода 'get_book_genre':

	1) test_get_book_genre_added_book
	- проверка получения жанра существующей книги 

	2)test_get_book_genre_not_added_book
	- проверка неполучения жанра несуществующей книги 

4. Тесты для метода 'get_books_with_specific_genre':

	1) test_get_books_with_specific_genre_set_genre_to_added_book
	- проверка получения списка книг по жанру из списка genre 

	2) test_get_books_with_specific_genre_not_available_genre
	- проверка неполучения списка книг по жанру не из списка genre

5. Тесты для метода 'get_books_for_children':

	1) test_get_books_for_children_by_not_genre_age_rating
	- проверка добавления книг в список books_for_children с жанром не из списка genre_age_rating

	2) test_get_books_for_children_by_genre_age_rating
	- проверка недобавления книг в список books_for_children с жанром из списка genre_age_rating

6. Тесты для метода 'add_book_in_favorites':

	1) test_add_book_in_favorites_add_book_from_book_genre
	- проверка добавления книги в список favorites из словаря books_genre

	2) test_add_book_in_favorites_add_added_book
	- проверка недобавления дубликата книги в список favorites

7. Тесты для метода 'delete_book_from_favorites':

	1)test_delete_book_from_favorites_added_book_in_favorites
	- проверка удаления книги из списка favorites
