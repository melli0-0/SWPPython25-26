from enum import Enum

class Books:
    total_books_created = 0
    def __init__(self, category, genre, title, pages):
        self.category = category
        self.genre = genre
        self.title = title
        self.pages = pages
        Books.total_books_created += 1

    def reading(self):
        print(f"{self.category} {self.title} is being read")


class EBooks(Books):
    def __init__(self, genre, title, pages):
        super().__init__("EBook", genre, title, pages)

    def reading(self):
        print(f"EBook with genre {self.genre.value} is being read")

    def loading(self):
        print(f"load {self.title}")

class Hardcover(Books):
    def __init__(self, genre, title, pages):
        super().__init__("Hardcover", genre, title, pages)


class Genres(Enum):
    FANTASY = "fantasy"
    THRILLER = "thriller"
    ROMANCE = "romance"
    SCIFI = "sci-fi"
    NONFICTION = "non-fiction"

class Main():
    book1 = EBooks(Genres.ROMANCE, "XMas Disaster", 290)
    book2 = Hardcover(Genres.FANTASY, "The Wooden Sword", 864)
    book3 = Books("Audiobook", Genres.NONFICTION, "Documentary about bees", None)

    print(f"total books {Books.total_books_created}")
    book2.reading()
    book1.loading()
    book1.reading()
    print(book3.pages)
    print(book2.title)

if __name__ == '__main__':
    Main()