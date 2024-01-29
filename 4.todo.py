class Book:
    """ Класс, описывающий объект Книга, который будет использоваться для книг, которые хранятся в библиотеке. """

    def __init__(self, pages: int):
        self.pages = pages  # TODO сделать атрибут защищеным, добавив нижнее подчеркивание вначале атрибута

    # Публичный метод, который внутри работает с защищенным атрибутом self._pages
    def get_pages(self) -> int:
        """Возвращает количество страниц в книге."""
        ...  # TODO реализовать возвращение значения защищенного атрибута

    # Публичный метод, который внутри работает с защищенным атрибутом self._pages
    def set_pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        ...  # TODO реализовать установку значения защищенному атрибуту


book = Book(200)
print(book.get_pages())
book.set_pages(300)
print(book.get_pages())


class Book:
    """ Класс, описывающий объект Книга, который будет использоваться для книг, которые хранятся в библиотеке. """

    def __init__(self, pages: int):
        self._pages = None  # делаем атрибут защищеным, добавив нижнее подчеркивание вначале атрибута
        self.set_pages(pages)  # устанавливаем с помощью метода значение количества страниц

    # Публичный метод, который внутри работает с защищенным атрибутом self._pages
    def get_pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    # Публичный метод, который внутри работает с защищенным атрибутом self._pages
    def set_pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages  # после всех проверок, устанавливаем значение защищенному атрибуту