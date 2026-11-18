import os
import json

# Save all JSON files in the same folder as this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

books = os.path.join(BASE_DIR, "books_info.json")
details = os.path.join(BASE_DIR, "student_register.json")
Issue = os.path.join(BASE_DIR, "issue_book.json")


# ---------- BOOK JSON FILE MANAGEMENT ----------

def create_book_db():
    if not os.path.exists(books):
        with open(books, "w") as f:
            json.dump([], f, indent=4)


def add_new_book(book_list):
    with open(books, "w") as file:
        json.dump(book_list, file, indent=4)


def load_books():
    create_book_db()
    with open(books, "r") as file:
        return json.load(file)


# ---------- STUDENT JSON FILE MANAGEMENT ----------

def create_student_db():
    if not os.path.exists(details):
        with open(details, "w") as file:
            json.dump({}, file, indent=4)


def load_data():
    create_student_db()
    with open(details, "r") as file:
        return json.load(file)


def add_data(students):
    with open(details, "w") as file:
        json.dump(students, file, indent=4)


# ---------- ISSUE BOOK RECORD MANAGEMENT ----------

def create_issue_db():
    if not os.path.exists(Issue):
        with open(Issue, "w") as file:
            json.dump([], file, indent=4)


def load_issued_book():
    create_issue_db()
    with open(Issue, "r") as file:
        return json.load(file)


def add_issued_book(issue_list):
    with open(Issue, "w") as file:
        json.dump(issue_list, file, indent=4)
        if __name__ == "__main__":
            create_book_db()
            create_student_db()
            create_issue_db()

            print("JSON Files Created Successfully!")