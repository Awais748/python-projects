class Book:
    total_books = 0 

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages  
        Book.total_books += 1

    def display_info(self):
        print(f"'{self.title}' by {self.author}, {self._pages} pages")

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value < 1:
            print("Pages must be at least 1!")
        else:
            self._pages = value

    @classmethod
    def book_count(cls):
        print(f"Total books: {cls.total_books}")

    @staticmethod
    def estimate_reading_time(pages):
        return pages * 2

    def __str__(self):
        return f"{self.title} by {self.author}, {self._pages} pages"



book1 = Book("Python Basics", "Awais T.", 150)
book2 = Book("Learn OOP", "Awais T.", 200)

book1.display_info()
book2.display_info()

book1.pages = 160
print(book1.pages) 

time = Book.estimate_reading_time(book2.pages)
print(f"Estimated reading time for '{book2.title}': {time} minutes")

print(book1)

Book.book_count()