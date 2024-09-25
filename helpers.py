from models import User, Category, Expense


def create_user(session):
    """Helper function to create a new user."""
    name = input("Enter user name: ").strip()
    if name:
        user = User(name=name)
        session.add(user)
        session.commit()
        print(f"User '{name}' created!")
    else:
        print("Invalid name. Try again.")


def get_all_users(session):
    """Helper function to display all users."""
    users = session.query(User).all()
    if users:
        print("\nList of Users:")
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}")
    else:
        print("No users found.")


def get_user_by_id(session):
    """Helper function to display a user by ID."""
    user_id = int(input("Enter user ID: "))
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        print(f"User ID: {user.id}, Name: {user.name}")
    else:
        print(f"User with ID {user_id} does not exist.")


def update_user(session):
    """Helper function to update a user."""
    user_id = int(input("Enter user ID: "))
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        new_name = input("Enter new name: ").strip()
        if new_name:
            user.name = new_name
            session.commit()
            print(f"User '{user.name}' updated!")
        else:
            print("Invalid name. Try again.")
    else:
        print(f"User with ID {user_id} does not exist.")


def delete_user(session):
    """Helper function to delete a user."""
    user_id = int(input("Enter user ID: "))
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User '{user.name}' deleted!")
    else:
        print(f"User with ID {user_id} does not exist.")


def create_category(session):
    """Helper function to create a new category."""
    name = input("Enter category name: ").strip()
    if name:
        category = Category(name=name)
        session.add(category)
        session.commit()
        print(f"Category '{name}' created!")
    else:
        print("Invalid category name. Try again.")


def get_all_categories(session):
    """Helper function to display all categories."""
    categories = session.query(Category).all()
    if categories:
        print("\nList of Categories:")
        for category in categories:
            print(f"ID: {category.id}, Name: {category.name}")
    else:
        print("No categories found.")


def get_category_by_id(session):
    """Helper function to display a category by ID."""
    category_id = int(input("Enter category ID: "))
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        print(f"Category ID: {category.id}, Name: {category.name}")
    else:
        print(f"Category with ID {category_id} does not exist.")


def update_category(session):
    """Helper function to update a category."""
    category_id = int(input("Enter category ID: "))
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        new_name = input("Enter new name: ").strip()
        if new_name:
            category.name = new_name
            session.commit()
            print(f"Category '{category.name}' updated!")
        else:
            print("Invalid category name. Try again.")
    else:
        print(f"Category with ID {category_id} does not exist.")


def delete_category(session):
    """Helper function to delete a category."""
    category_id = int(input("Enter category ID: "))
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category '{category.name}' deleted!")
    else:
        print(f"Category with ID {category_id} does not exist.")


def create_expense(session):
    """Helper function to add an expense."""
    try:
        user_id = int(input("Enter user ID: "))
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            print(f"User with ID {user_id} does not exist.")
            return

        category_id = int(input("Enter category ID: "))
        category = session.query(Category).filter_by(id=category_id).first()
        if not category:
            print(f"Category with ID {category_id} does not exist.")
            return

        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description (optional): ")

        expense = Expense(user_id=user_id,
                          category_id=category_id,
                          amount=amount,
                          description=description)
        session.add(expense)
        session.commit()
        print(
            f"Expense of {amount} added for user {user.name} in category {category.name}."
        )
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def get_all_expenses(session):
    """Helper function to display all expenses."""
    expenses = session.query(Expense).all()
    if expenses:
        print("\nList of expenses:")
        for expense in expenses:
            print(
                f"ID: {expense.id}, Amount: {expense.amount}, Description: {expense.description}, "
                f"User ID: {expense.user_id}, Category ID: {expense.category_id}"
            )
    else:
        print("No expenses found.")


def get_expense_by_id(session):
    """Helper function to display an expense by ID."""
    expense_id = int(input("Enter expense ID: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        print(
            f"ID: {expense.id}, Amount: {expense.amount}, Description: {expense.description}, "
            f"User ID: {expense.user_id}, Category ID: {expense.category_id}")
    else:
        print(f"Expense with ID {expense_id} does not exist.")


def update_expense(session):
    """Helper function to update an expense."""
    expense_id = int(input("Enter expense ID: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        new_amount = float(input("Enter new amount: "))
        if new_amount:
            expense.amount = new_amount
            session.commit()
            print(f"Expense amount updated to {new_amount}.")
        else:
            print("Invalid amount. Try again.")
    else:
        print(f"Expense with ID {expense_id} does not exist.")


def delete_expense(session):
    """Helper function to delete an expense."""
    expense_id = int(input("Enter expense ID: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print(f"Expense with ID {expense_id} deleted.")
    else:
        print(f"Expense with ID {expense_id} does not exist.")
