class Book:
    def __init__(self, books, books1, books2):
        self.books = books
        self._books = books1
        self.__books = books2
    def get_book_from_id(self, id: int):
        return self.books[id]

# это делает пользователь
b = Book(1, 2, 3)
print(b._books)
b._books = 4        # изменил
print(b._books)

class Book:
    def __init__(self, books1: list, books2):
        self._books = None
        self.set_books(books1)
        self.__books = books2

    def get_book_from_id(self, id: int): # чтобы получить
        return self._books[id]

    def set_books(self, value: list):    # чтобы установить
        if not isinstance(value, list):
            raise TypeError("Должно быть типа list")
        self._books = value

    def get_books(self):
        return self._books

# это делает пользователь
b = Book([2, 5], 3)
print(b._books)
b._books = 4        # изменил
print(b._books)
print(b.get_books())
print(b.set_books([]))
