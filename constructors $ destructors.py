class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        print("Book '" + self.title + "' created")

    def _del_(self):
        print("Book '" + self.title + "' removed")


book1 = Book("Python Basics", "John")
book2 = Book("Data Science", "Alice")

del book1

print("Library is still open")

del book2
