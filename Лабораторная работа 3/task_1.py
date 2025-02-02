class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} . Кол-во страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()} . Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value


if __name__ == '__main__':
    book = Book("Мастер и Маргарита", "Булгаков")
    print(book)
    print(repr(book))

    paper_book = PaperBook("Мертвые души", "Гоголь", 350)
    print(paper_book)
    print(repr(paper_book))

    audio_book = AudioBook("1984", "Оруэлл", 12.5)
    print(audio_book)
    print(repr(audio_book))

    try:
        paper_book.pages = "abc"
    except TypeError as e:
        print(e)

    try:
        paper_book.pages = -10
    except ValueError as e:
        print(e)

    try:
        audio_book.duration = "abc"
    except TypeError as e:
        print(e)

    try:
        audio_book.duration = -10
    except ValueError as e:
        print(e)

    try:
        book.name = 'new_name'
    except AttributeError as e:
        print(e)
