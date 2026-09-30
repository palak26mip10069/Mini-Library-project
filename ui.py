import core
def add_book():
    book = input("Enter book name: ")
    core.add_book_logic(book)
    print("Book added successfully!")
def display_books():
    books = core.get_all_books()
    if len(books) == 0:
        print("No books available.")
    else:
        print("Books in Library:")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
def search_book():
    book = input("Enter book name to search: ")
    if core.search_book_logic(book):
        print("Book is available.")
    else:
        print("Book is not available.")
def issue_book():
    book = input("Enter book name to issue: ")
    if core.issue_book_logic(book):
        print("Book issued successfully!")
    else:
        print("Book is not available.")
def return_book():
    book = input("Enter book name to return: ")
    core.return_book_logic(book)
    print("Book returned successfully!")
