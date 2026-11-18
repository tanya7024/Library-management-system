from jsonfile_manager import *


def return_book():
    issue_info = load_issued_book()
    books = load_books()

    if not issue_info:
        print("No Issued Records found")
        return

    std_id = input("Enter student ID: ")
    book_id = input("Enter book ID to return: ")
    date = input("Enter book issue date (dd/mm/yyyy): ")

    target_issue = None
    for issue in issue_info:
        if (issue["Student_ID"].lower() == std_id.lower() and
                issue["Book_ID"].lower() == book_id.lower() and
                issue["Date"] == date):
            target_issue = issue
            break

    if target_issue:
        issue_info.remove(target_issue)
        add_issued_book(issue_info)

        for book in books:
            if book["Book_ID"].lower() == book_id.lower():
                book["No_Copies"] += 1
                break
        add_new_book(books)
        print("Book returned successfully!")
    else:
        print("Issued Record not found")