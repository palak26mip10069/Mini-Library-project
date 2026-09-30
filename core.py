import storage
def add_book_logic(book):
    storage.books.append(book)
def get_all_books():
    return storage.books
def search_book_logic(book):
    return book in storage.books
def issue_book_logic(book):
    if book in storage.books:
        storage.books.remove(book)
        return True
    return False
def return_book_logic(book):
    storage.books.append(book)
