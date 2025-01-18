BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
    Класс, представляющий книгу с атрибутами id, name и pages.
    """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор для инициализации объекта Book.

        Args:
            id_: Идентификатор книги.
            name: Название книги.
            pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги в формате "Книга \"название_книги\"".

        Returns:
            Строка с описанием книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта, которое может быть использовано для
        создания нового экземпляра класса Book.

        Returns:
            Строка в формате "Book(id_={self.id}, name='{self.name}', pages={self.pages})".
        """
        return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    """
    Класс, представляющий библиотеку с книгами.
    """

    def __init__(self, books: list[Book] = None):
        """
        Конструктор для инициализации объекта Library.

        Args:
            books: Список книг (объектов Book).
            По умолчанию - пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.
        Если книг в библиотеке нет, то вернуть 1.
        Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.

        Returns:
            Следующий доступный идентификатор книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса.
        Если книга существует, то вернуть индекс из списка.
        Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует".

        Args:
            book_id: Идентификатор книги.

        Returns:
            Индекс книги в списке.

        Raises:
            ValueError: Если книга с запрашиваемым id не найдена.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
