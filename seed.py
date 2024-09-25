from models import User, session, Category, Expense
from faker import Faker
import random

fake = Faker()


def reset_database():
    models = [User, Category]
    for model in models:
        session.query(model).delete()


def seed_data():
    users = []
    for _ in range(10):
        user_name = fake.unique.name()

        user = User(name=user_name)

        users.append(user)
        session.add(user)
        session.commit()

    categories = []
    category_names = [
        "Food and Groceries", "Transportation", "Utilities", "Entertainment",
        "Healthcare"
    ]
    for name in category_names:
        category_name = name

        category = Category(name=category_name)

        categories.append(category)
        session.add(category)
        session.commit()

    expenses = []
    for _ in range(20):
        expense_amount = fake.pydecimal(left_digits=4,
                                        right_digits=2,
                                        positive=True)
        expense_description = fake.unique.sentence(nb_words=6)
        expense_user_id = random.choice(users).id
        expense_category_id = random.choice(categories).id

        expense = Expense(description=expense_description,
                          amount=expense_amount,
                          user_id=expense_user_id,
                          category_id=expense_category_id)
        expenses.append(expense)
        session.add(expense)
    session.commit()


if __name__ == '__main__':
    print("Seeding data...")
    reset_database()
    seed_data()
    print("Seeding done!")
