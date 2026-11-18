from jsonfile_manager import *


def delete_book():
    books = load_books()
    if not books:
        print("Library is empty.")
        return

    book_id = input("Enter Book ID to delete: ")
    updated_books = [b for b in books if b["Book_ID"].lower() != book_id.lower()]

    if len(updated_books) < len(books):
        add_new_book(updated_books)
        print("Book deleted successfully!")
    else:
        print("Book ID not found.")