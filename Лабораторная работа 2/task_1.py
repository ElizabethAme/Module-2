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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
