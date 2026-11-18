from jsonfile_manager import *


def search_book():
    books_info = load_books()
    if not books_info:
        print("Library is empty.")
        return

    print("\n1. For search by Book ID")
    print("2. For search by Book Name")
    print("3. For search by Book Author Name")
    try:
        n = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice!")
        return

    print("\n")
    if n == 1:
        query = input("Enter Book ID: ").lower()
        found = [b for b in books_info if b["Book_ID"].lower() == query]
    elif n == 2:
        query = input("Enter Book Name: ").lower()
        found = [b for b in books_info if b["Book_Name"].lower() == query]
    elif n == 3:
        query = input("Enter Book Author: ").lower()
        found = [b for b in books_info if b["Book_Author"].lower() == query]
    else:
        print("Invalid choice!")
        return

    if found:
        for book in found:
            print("-" * 20)
            for k, v in book.items():
                print(f"{k}: {v}")
    else:
        print("No matching record found.")