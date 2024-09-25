import sys
from database import create_tables, session
from helpers import (create_user, get_all_users, get_user_by_id, update_user,
                     delete_user, create_category, get_all_categories,
                     get_category_by_id, update_category, delete_category,
                     create_expense, get_all_expenses, get_expense_by_id,
                     update_expense, delete_expense)

# Initialize the tables
create_tables()


def main_menu():
    """Display the main menu and handle user input."""
    print("\nExpense Tracker CLI")
    print("=================================")
    print("0. Exit!")
    print("1. Create user")
    print("2. List all users")
    print("3. List user by id")
    print("4. Update user")
    print("5. Delete user")
    print("6. Create category")
    print("7. List all categories")
    print("8. List category by id")
    print("9. Update category")
    print("10. Delete category")
    print("11. Create expense")
    print("12. List all expenses")
    print("13. List expense by id")
    print("14. Update expense")
    print("15. Delete expense")
    print("=================================")


def run():
    """Main loop for running the CLI."""

    while True:
        main_menu()
        choice = input("Choose an option: ")

        if choice == '0':
            sys.exit()
        elif choice == '1':
            create_user(session)
        elif choice == '2':
            get_all_users(session)
        elif choice == '3':
            get_user_by_id(session)
        elif choice == '4':
            update_user(session)
        elif choice == '5':
            delete_user(session)
        elif choice == '6':
            create_category(session)
        elif choice == '7':
            get_all_categories(session)
        elif choice == '8':
            get_category_by_id(session)
        elif choice == '9':
            update_category(session)
        elif choice == '10':
            delete_category(session)
        elif choice == '11':
            create_expense(session)
        elif choice == '12':
            get_all_expenses(session)
        elif choice == '13':
            get_expense_by_id(session)
        elif choice == '14':
            update_expense(session)
        elif choice == '15':
            delete_expense(session)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    run()
