class Book:
    """Базовый класс книги"""
    def __init__(self, author: str = 'Пушкин А. С.', pages: int = 500):
        self.author = author
        self.pages = pages

class PaperBook(Book):
    """Бумажная книга"""
    cover: str = "Твердый переплет"

class EBook(Book):
    """Оцифрованная книга"""
    format: str = "pdf"

# вместо
# print(PaperBook.pages)  # унаследованные атрибут
# print(EBook.pages)  # унаследованные атрибут
print(PaperBook().pages)  # () инициализация
print(EBook().pages)  # () инициализация

print(PaperBook.cover)  # атрибут только класса PaperBook
print(EBook.format)  # атрибут только класса EBook

print(PaperBook(pages=345).pages)


class Book:
    """Базовый класс книги"""
    def __init__(self, author: str = 'Пушкин А. С.', pages: int = 500):
        self.author = author
        self.pages = pages

class PaperBook(Book):
    """Бумажная книга"""
    def __init__(self, author, pages, cover: str = "Твердый переплет"):
        super().__init__(author, pages)
        self.cover = cover

class EBook(Book):
    """Оцифрованная книга"""
    format: str = "pdf"

print(PaperBook(author="1", pages=11))  #
print(EBook().pages)  #

print(PaperBook(author="1", pages=11).cover)  # атрибут только класса PaperBook
print(EBook.format)  # атрибут только класса EBook

print(PaperBook(author="123", pages=345).pages)
