class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("You borrowed", self.title)
        else:
            print("Book is not available.")


book = LibraryBook("A Journey Home")
book.borrow()
