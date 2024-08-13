class Book:
    # Class constant for genre names
    GENRES = [
        "Romance", "Mystery", "Science Fiction", "Thriller", 
        "Young Adult", "Children’s Fiction", "Self-help", 
        "Fantasy", "Historical Fiction", "Poetry"
    ]

    def __init__(self, isbn, title, author, genre, available):
        # Initialize attributes
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available

    # Getters for attributes
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_available(self):
        return self.__available

    # Additional getter for genre name
    def get_genre_name(self):
        return Book.GENRES[self.__genre]

    # Additional getter for availability status
    def get_availability(self):
        return "Available" if self.__available else "Borrowed"

    # Setters for attributes
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        if 0 <= genre < len(Book.GENRES):
            self.__genre = genre
        else:
            raise ValueError("Invalid genre index")

    # Methods to borrow or return a book
    def borrow_it(self):
        self.__available = False

    def return_it(self):
        self.__available = True

    # String representation of the book
    def __str__(self):
        return "{:14s} {:25s} {:25s} {:20s} {:s}".format(
            self.__isbn, self.__title, self.__author, 
            self.get_genre_name(), self.get_availability()
        )
