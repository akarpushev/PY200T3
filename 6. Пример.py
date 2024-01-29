class Book:
    def __init__(self, books1: list, books2):
        self._books = books1
        self.__books = books2

    def get_book_from_id(self, id: int, value): # чтобы получить
        return self._books[id]

    def funk(self, value: list):
        self._books = value # вызывает setter
        return self._books

    # def get_books(self):
    #     return self._books
    # вместо этого пишем
    @property
    def books(self):
        print("Вызван getter")
        return self._books

    @books.setter
    def books(self, value):
        print("Вызван setter")
        if not isinstance(value, list):
            raise TypeError("Должно быть типа list")
        self._books = value

b = Book([2, 5], 3)
print(b._books)
b._books = 4        # изменил
print(b._books)
# вместо print(b.get_books())
print(b.books)

# b.books = [1, 1, 6] не дает устанавить пока нет setter
b._books = [1, 1, 6]
print(b._books)
#b.books = 33
#print(b.books)
#print(b._books)
#print(b.books[13])
b.books = [333]
print(b.__dict__)

b.funk('123a')
print(b.books)