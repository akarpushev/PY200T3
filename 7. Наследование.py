# **Наследование** — способность класса базироваться на другом классе.
# Это главный механизм для повторного использования кода.

class Book:
    """Базовый класс книги"""
    author: str = 'Пушкин А. С.'
    pages: int = 500

class PaperBook(Book):
    """Бумажная книга"""
    cover: str = "Твердый переплет"

class EBook(Book):
    """Оцифрованная книга"""
    format: str = "pdf"

print(PaperBook.pages)  # унаследованные атрибут
print(EBook.pages)  # унаследованные атрибут

print(PaperBook.cover)  # атрибут только класса PaperBook
print(EBook.format)  # атрибут только класса EBook