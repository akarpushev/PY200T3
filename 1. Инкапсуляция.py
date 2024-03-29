# Инкапсуляция — упаковка данных и методов для их обработки вместе, т. е. в классе.
# И при необходимости разграничения доступа к ним.

# если надо проверять присваиваемое полю значение на корректность,
# то делать это каждый раз в основном коде программы будет нехорошо.
class Book:
    """ Класс, описывающий объект Книга, который будет использоваться для книг, которые хранятся в библиотеке. """
    def __init__(self, pages: int):
        self.pages = pages

book = Book(500)
new_pages = 501
if not isinstance(new_pages, int):  # проверки вне класса
    raise TypeError("Количество страниц должно быть типа int")
else:
    book.pages = new_pages

# Проверочный код должен быть помещен в метод, который получает данные для присвоения полю.

class Book:
    """ Класс, описывающий объект Книга, который будет использоваться для книг, которые хранятся в библиотеке. """
    def __init__(self, pages: int):
        self.pages = None
        self.set_pages(pages)  # обращаемся к атрибуту через метод

    def set_pages(new_pages: int):
        # все необходимые проверки
        self.pages = new_pages

book = Book(500)

new_pages = 501
book.set_pages(new_pages)  # обращаемся к атрибуту через метод

#А само поле должно быть **закрыто** для доступа из вне класса.
#В этом случае ему невозможно будет присвоить недопустимое значение.

