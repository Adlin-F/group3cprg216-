import csv
from book import Book

def load_books(filename):
    books = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                isbn, title, author, genre, available = row
                genre = int(genre)
                available = available.strip().lower() == "true"
                books.append(Book(isbn, title, author, genre, available))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return books

def save_books(filename, books):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for book in books:
            writer.writerow([
                book.get_isbn(),
                book.get_title(),
                book.get_author(),
                book.get_genre(),
                "True" if book.get_available() else "False"
            ])

def find_book_by_isbn(book_list, isbn):
    for book in book_list:
        if book.get_isbn() == isbn:
            return book
    return None

def display_main_menu():
    options = {
        "1": "Search for books",
        "2": "Borrow a book",
        "3": "Return a book"
    }
    print("\nReader's Guild Library - Main Menu")
    print("=" * len("Reader's Guild Library - Main Menu"))
    for key, option in options.items():
        print(f"{key}. {option}")
    print("0. Exit the system")

def display_librarian_menu():
    options = {
        "1": "Search for books",
        "2": "Borrow a book",
        "3": "Return a book",
        "4": "Add a book",
        "5": "Remove a book",
        "6": "Print catalog"
    }
    print("\nReader's Guild Library - Librarian Menu")
    print("=" * len("Reader's Guild Library - Librarian Menu"))
    for key, option in options.items():
        print(f"{key}. {option}")
    print("0. Exit the system")

def search_books(book_list, search_value):
    search_value = search_value.lower()
    found_books = [book for book in book_list if (
        search_value in book.get_title().lower() or
        search_value in book.get_author().lower() or
        search_value in book.get_genre_name().lower() or
        search_value in book.get_isbn()
    )]

    if not found_books:
        print("No matching books found.")
        return

    print("{:<15} {:<30} {:<30} {:<20} {:<10}".format(
        "ISBN", "Title", "Author", "Genre", "Availability"
    ))
    print("-" * 110)
    for book in found_books:
        print(book)

def borrow_book(book_list, isbn):
    book = find_book_by_isbn(book_list, isbn)
    if book:
        if book.get_available():
            book.borrow_it()
            print(f"'{book.get_title()}' with ISBN {isbn} successfully borrowed.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently available.")
    else:
        print("No book found with that ISBN.")

def return_book(book_list, isbn):
    book = find_book_by_isbn(book_list, isbn)
    if book:
        if not book.get_available():
            book.return_it()
            print(f"'{book.get_title()}' with ISBN {isbn} successfully returned.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently borrowed.")
    else:
        print("No book found with that ISBN.")

def add_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    while len(isbn) != 13 or not isbn.isdigit():
        print("Invalid ISBN format. Please enter a valid 13-digit ISBN.")
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    title = input("Enter title: ")
    author = input("Enter author name: ")
    
    genre_options = Book.GENRES
    genre = input(f"Enter genre (choices are: {', '.join(genre_options)}): ")
    while genre not in genre_options:
        print(f"Invalid genre. Choices are: {', '.join(genre_options)}")
        genre = input("Enter genre: ")
    
    genre_index = genre_options.index(genre)

    available = True
    book_list.append(Book(isbn, title, author, genre_index, available))
    print(f"'{title}' with ISBN {isbn} successfully added.")

def remove_book(book_list, isbn):
    book = find_book_by_isbn(book_list, isbn)
    if book:
        book_list.remove(book)
        print(f"'{book.get_title()}' with ISBN {isbn} successfully removed.")
    else:
        print("No book found with that ISBN.")

def print_catalog(book_list):
    print("{:<15} {:<30} {:<30} {:<20} {:<10}".format(
        "ISBN", "Title", "Author", "Genre", "Availability"
    ))
    print("-" * 110)
    for book in book_list:
        print(book)

def main():
    filename = input("Enter book catalog filename: ")
    book_list = load_books(filename)

    while not book_list:
        print("File not found.")
        filename = input("Re-enter book catalog filename: ")
        book_list = load_books(filename)

    print("Book catalog has been loaded.")
    
    passcode = "2130"
    is_librarian = False

    while True:
        if is_librarian:
            display_librarian_menu()
            choice = input("Enter your selection: ").strip()
            if choice == "1":
                search_value = input("-- Search for books --\nEnter search value: ")
                search_books(book_list, search_value)
            elif choice == "2":
                isbn = input("-- Borrow a book --\nEnter the 13-digit ISBN (format 999-9999999999): ")
                borrow_book(book_list, isbn)
            elif choice == "3":
                isbn = input("-- Return a book --\nEnter the 13-digit ISBN (format 999-9999999999): ")
                return_book(book_list, isbn)
            elif choice == "4":
                add_book(book_list)
            elif choice == "5":
                isbn = input("-- Remove a book --\nEnter the 13-digit ISBN (format 999-9999999999): ")
                remove_book(book_list, isbn)
            elif choice == "6":
                print_catalog(book_list)
            elif choice == "0":
                print("-- Exit the system --")
                save_books(filename, book_list)
                print("Book catalog has been saved.")
                print("Good Bye!")
                break
            else:
                print("Invalid option")
        else:
            display_main_menu()
            choice = input("Enter your selection: ").strip()
            if choice == "1":
                search_value = input("-- Search for books --\nEnter search value: ")
                search_books(book_list, search_value)
            elif choice == "2":
                isbn = input("-- Borrow a book --\nEnter the 13-digit ISBN (format 999-9999999999): ")
                borrow_book(book_list, isbn)
            elif choice == "3":
                isbn = input("-- Return a book --\nEnter the 13-digit ISBN (format 999-9999999999): ")
                return_book(book_list, isbn)
            elif choice == "0":
                print("-- Exit the system --")
                save_books(filename, book_list)
                print("Book catalog has been saved.")
                print("Good Bye!")
                break
            elif choice == passcode:
                is_librarian = True
                print("Librarian menu unlocked.")
            else:
                print("Invalid option")

if __name__ == "__main__":
    main()
