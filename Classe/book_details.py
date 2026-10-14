class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)


my_book = Book("The Blue Planet", "Sam Lee")
my_book.show_details()
