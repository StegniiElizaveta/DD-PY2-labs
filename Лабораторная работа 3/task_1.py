class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__()
        self.pages = pages
        @property
        def pages(self) -> int:
            return self._pages

        @pages.setter
        def pages(self, new_pages: int):
            if type(new_pages) != int:
                raise TypeError
            else:
                self._pages = new_pages

    super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__()

        self.duration = duration

        @property
        def duration(self) -> float:
            return self._duration

        @duration.setter
        def pages(self, new_pages: float):
            if type(duration) != float:
                raise TypeError
            else:
                self._duration = duration

    super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

book = Book('lala', 'hhh')
print(book.name)
#проверка, работает ли геттер
#пройдена

