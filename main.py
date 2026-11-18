from new_book import add_book, display_all_book
from student_register import student_register
from delete_book import delete_book
from search_book import search_book
from issue_book import issue_book, display_issue_book
from return_book import return_book


def main():
    while True:
        print("\n" + "=" * 30)
        print("      LIBRARY SYSTEM       ")
        print("=" * 30)
        print("1. ADD NEW BOOK")
        print("2. DISPLAY ALL BOOKS")
        print("3. SEARCH FOR A BOOK")
        print("4. STUDENT REGISTRATION")
        print("5. ISSUE BOOK")
        print("6. RETURN BOOK")
        print("7. DISPLAY ISSUED BOOKS")
        print("8. DELETE A BOOK")
        print("9. EXIT")

        try:
            option = int(input("Enter your option number (1 to 9): "))
        except ValueError:
            print("Please enter a valid integer between 1 and 9.")
            continue

        if option == 1:
            add_book()
        elif option == 2:
            display_all_book()
        elif option == 3:
            search_book()
        elif option == 4:
            student_register()
        elif option == 5:
            issue_book()
        elif option == 6:
            return_book()
        elif option == 7:
            display_issue_book()
        elif option == 8:
            delete_book()
        elif option == 9:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid option! Please choose between 1 to 9.")


if __name__ == "__main__":
    main()