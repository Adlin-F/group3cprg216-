 def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available

    # Getters
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

    def get_genre_name(self):
        return Book.GENRE_NAMES.get(self.__genre, "Unknown Genre")

    def get_availability(self):
        return 'Available' if self.__available else 'Borrowed'

    # Setters
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre

    def borrow_it(self):
        self.__available = False

    def return_it(self):
        self.__available = True

    def __str__(self):
        return f"{self.__isbn} {self.__title} {self.__author} {self.get_genre_name()} {self.get_availability()}"
