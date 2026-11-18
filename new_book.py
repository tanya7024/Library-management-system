from jsonfile_manager import *


def add_book():
    n = int(input("Enter the number of books you want to add: "))
    books = load_books()
    for _ in range(n):
        book_id = input("Enter the ID of the book: ")
        name = input("Enter the name of the book: ")
        author = input("Enter the author of the book: ")
        category = input("Enter the category of the book: ")
        n_copies = int(input("Enter the number of copies of the book: "))

        d = {
            "Book_ID": book_id,
            "Book_Name": name,
            "Book_Author": author,
            "Book_Category": category,
            "No_Copies": n_copies
        }
        books.append(d)
    add_new_book(books)
    print("Books added successfully!")


def display_all_book():
    books = load_books()
    if not books:
        print("Library is empty.")
        return
    for book in books:
        print("\n" + "-" * 20)
        for k, v in book.items():
            print(f"{k}: {v}")