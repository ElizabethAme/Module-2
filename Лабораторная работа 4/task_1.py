from typing import List, Optional, ClassVar

class SocialNetwork:
    """
    Базовый класс, представляющий социальную сеть.
    """

    _total_networks: ClassVar[int] = 0  # Приватный атрибут класса, отслеживающий общее количество сетей.

    def __init__(self, name: str, founder: str, year_founded: int) -> None:
        """
        Конструктор класса SocialNetwork.

        :param name: Название социальной сети.
        :param founder: Имя основателя.
        :param year_founded: Год основания.
        """
        self.name = name
        self.founder = founder
        self.year_founded = year_founded
        self._users: List[str] = []  # Список пользователей социальной сети (защищенный атрибут)
        SocialNetwork._total_networks += 1

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта SocialNetwork.
        """
        return f"{self.name} - основана {self.founder} в {self.year_founded} году"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта SocialNetwork для отладки.
        """
        return f"SocialNetwork(name='{self.name}', founder='{self.founder}', year_founded={self.year_founded})"

    def add_user(self, username: str) -> None:
        """
        Добавляет нового пользователя в социальную сеть.
        """
        self._users.append(username)

    def get_user_count(self) -> int:
        """
        Возвращает количество пользователей в социальной сети.
        """
        return len(self._users)

    def get_info(self) -> str:
        """
        Возвращает общую информацию о социальной сети.
        """
        return f"Социальная сеть '{self.name}', количество пользователей: {self.get_user_count()}"

    @classmethod
    def get_total_networks(cls) -> int:
        """
        Возвращает общее количество созданных социальных сетей.
        """
        return cls._total_networks


class VK(SocialNetwork):
    """
    Дочерний класс, представляющий социальную сеть VK.
    """

    def __init__(self, founder: str, year_founded: int) -> None:
        """
        Конструктор класса VK.  Имя сети фиксировано.

        :param founder: Имя основателя.
        :param year_founded: Год основания.
        """
        super().__init__(name="VK", founder=founder, year_founded=year_founded)
        self.domain = "vk.com" # Добавляем атрибут домена

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта VK. Переопределяет метод __str__ базового класса.
        """
        return f"VK - основана {self.founder} в {self.year_founded} году.  Доступна по адресу: {self.domain}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта VK для отладки. Переопределяет метод __repr__ базового класса.
        """
        return f"VK(founder='{self.founder}', year_founded={self.year_founded})"

    def get_info(self) -> str:
        """
        Возвращает информацию о социальной сети VK. Переопределяет метод get_info базового класса.
        Переопределение необходимо, чтобы добавить информацию о домене.
        """
        base_info = super().get_info() # Получаем информацию от базового класса
        return f"{base_info}, Домен: {self.domain}"

    def post_message(self, username: str, message: str) -> str:
        """
        Позволяет пользователю отправить сообщение.
        """
        return f"{username} опубликовал сообщение в VK: '{message}'"

    def add_user(self, username: str, group: Optional[str] = None) -> None:
        """
        Добавляет пользователя в VK и, опционально, в группу.
        Переопределяет метод add_user базового класса.
        Переопределение необходимо, для того, чтобы добавить пользователя сразу в группу.
        """
        super().add_user(username)
        if group:
            print(f"Пользователь {username} добавлен в группу {group} VK.")


if __name__ == "__main__":
    network1 = SocialNetwork("MyNetwork", "John Doe", 2023)
    print(network1) # MyNetwork - основана John Doe в 2023 году
    print(repr(network1)) # SocialNetwork(name='MyNetwork', founder='John Doe', year_founded=2023)
    network1.add_user("Alice")
    network1.add_user("Bob")
    print(network1.get_info()) # Социальная сеть 'MyNetwork', количество пользователей: 2

    vk1 = VK("Павел Дуров", 2006)
    print(vk1) # VK - основана Павел Дуров в 2006 году.  Доступна по адресу: vk.com
    print(repr(vk1)) # VK(founder='Павел Дуров', year_founded=2006)
    vk1.add_user("Иван")
    vk1.add_user("Мария", group="Python Developers")
    print(vk1.get_info()) # Социальная сеть 'VK', количество пользователей: 2, Домен: vk.com
    print(vk1.post_message("Иван", "Привет всем!")) # Иван опубликовал сообщение в VK: 'Привет всем!'

    print(f"Всего социальных сетей: {SocialNetwork.get_total_networks()}") # Всего социальных сетей: 2