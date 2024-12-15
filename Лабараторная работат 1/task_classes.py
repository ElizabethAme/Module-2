from typing import Union
import doctest


class Window:
    def __init__(self, width: Union[int, float], height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Окно".

        :param width: Ширина окна в сантиметрах. Должна быть положительным числом.
        :param height: Высота окна в сантиметрах. Должна быть положительным числом.

        :raises ValueError: Если ширина или высота отрицательные.
        :raises TypeError: Если ширина или высота не целые или десятичные числа.

        Пример:
        >>> w = Window(100, 150)
        >>> w.width
        100
        >>> w.height
        150
        """
        if width <= 0:
            raise ValueError("Ширина окна должна быть положительным числом.")
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина окна должна быть целым, либо десятичным числом.")
        self.width = width

        if height <= 0:
            raise ValueError("Высота окна должна быть положительным числом.")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота окна должна быть целым, либо десятичным числом.")
        self.height = height

    def open_window(self) -> None:
        """
        Открыть окно.
        Эта функция не принимает никаких параметров и не возвращает значения.

        Пример:
        >>> w = Window(100, 150)
        >>> w.open_window()  # просто проверка без ошибок
        """
        pass
        ...

    def close_window(self) -> None:
        """
        Закрыть окно.
        Эта функция не принимает никаких параметров и не возвращает значения.

        Пример:
        >>> w = Window(100, 150)
        >>> w.close_window()  # просто проверка без ошибок
        """
        pass
        ...


class Table:
    def __init__(self, length: Union[int, float], width: Union[int, float], material: str):
        """
        Создание и подготовка к работе объекта "Стол".

        :param length: Длина стола в сантиметрах. Должна быть положительным числом.
        :param width: Ширина стола в сантиметрах. Должна быть положительным числом.
        :param material: Материал, из которого изготовлен стол.

        :raises ValueError: Если длина или ширина отрицательные.
        :raises TypeError: Если длина или ширина не целые или десятичные числа. Если материал стола не строка.

        Пример:
        >>> t = Table(200, 80, "Дерево")
        >>> t.length
        200
        >>> t.material
        'Дерево'
        """
        if length <= 0:
            raise ValueError("Длина стола должна быть положительным числом.")
        if not isinstance(length, (int, float)):
            raise TypeError("Длина стола должна быть целым, либо десятичным числом.")
        self.length = length

        if width <= 0:
            raise ValueError("Ширина стола должна быть положительным числом.")
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должна быть целым, либо десятичным числом.")
        self.width = width

        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть записан текстом.")
        self.material = material

    def clean_table(self) -> None:
        """
        Убрать со стола.
        Эта функция не принимает никаких параметров и не возвращает значения.

        >>> t = Table(200, 80, "Дерево")
        >>> t.clean_table()  # просто проверка без ошибок
        """
    pass

    def resize(self, new_length: Union[int, float], new_width: Union[int, float]) -> None:
        """
        Изменить размеры стола.

        :param new_length: Новая длина стола в сантиметрах. Должна быть положительным числом.
        :param new_width: Новая ширина стола в сантиметрах. Должна быть положительным числом.

        :raises ValueError: Если новая длина или ширина отрицательные.

        Пример:
        >>> t.resize(250, 100)
        ...
        """
        if new_length <= 0 or new_width <= 0:
            raise ValueError("Длина и ширина стола должны быть положительными числами.")

        self.length = new_length
        self.width = new_width


class Vase:
    def __init__(self, height: Union[int, float], capacity: Union[int, float], color: str):
        """
        Создание и подготовка к работе объекта "Ваза".

        :param height: Высота вазы в сантиметрах. Должна быть положительным числом.
        :param capacity: Вместимость вазы в литрах. Должна быть положительным числом.
        :param color: Цвет вазы.

        :raises ValueError: Если высота или вместимость отрицательные.
        :raises TypeError: Если высота или вместимость не целое или десятичное число. Если цвет записан не текстом

        Пример:
        >>> v = Vase(30, 2, "Синий")
        >>> v.height
        30
        >>> v.color
        'Синий'
        """
        if height <= 0:
            raise ValueError("Высота вазы должна быть положительным числом.")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота вазы должна быть целым, либо десятичным числом.")
        self.height = height

        if capacity <= 0:
            raise ValueError("Вместимость вазы должна быть положительным числом.")
        if not isinstance(capacity, (int, float)):
            raise TypeError("Вместимость вазы должна быть целым, либо десятичным числом.")
        self.capacity = capacity

        if not isinstance(color, str):
            raise TypeError("Цвет стола должен быть записан текстом.")
        self.color = color

    def fill(self, amount: Union[int, float]) -> None:
        """
        Заполнить вазу.

        :param amount: Объем для заполнения в литрах, не должен быть отрицательным.

        :raises ValueError: Если amount отрицателен.

        Примеры:
        >>> v = Vase(30, 2, "Синий")
        >>> v.fill(1.5)
        Просто проверка без ошибок
        >>> v.fill(-0.5)
        Это вызовет ValueError
        """
        if amount < 0:
            raise ValueError("Объем для заполнения должен быть неотрицательным.")

    def empty(self) -> None:
        """
        Опустошить вазу.
        Эта функция не принимает никаких параметров и не возвращает значения.

        >>> v = Vase(30, 2, "Синий")
        >>> v.empty()  # просто проверка без ошибок
        """
        pass


if __name__ == "__main__":
    doctest.testmod()
