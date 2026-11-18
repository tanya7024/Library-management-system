from jsonfile_manager import *


def issue_book():
    std_id = input("Enter student ID: ")
    book_id = input("Enter book ID: ")

    std_info = load_data()
    book_info = load_books()
    issue_info = load_issued_book()

    if std_id not in std_info:
        print("Student is not Registered")
        return

    target_book = None
    for book in book_info:
        if book["Book_ID"].lower() == book_id.lower():
            target_book = book
            break

    if target_book and target_book["No_Copies"] > 0:
        target_book["No_Copies"] -= 1
        date = input("Enter date of book issue (dd/mm/yyyy): ")

        issue_record = {
            "Student_ID": std_id,
            "Book_ID": book_id,
            "Date": date
        }
        issue_info.append(issue_record)

        add_issued_book(issue_info)
        add_new_book(book_info)
        print("Book issued successfully!")
    else:
        print("Book is not available or out of stock.")


def display_issue_book():
    issues = load_issued_book()
    if not issues:
        print("No issued records found.")
        return
    for issue in issues:
        print("-" * 20)
        for k, v in issue.items():
            print(f"{k}: {v}")