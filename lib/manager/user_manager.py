from db.models import Session, User
import click

class UserManager:
    def __init__(self):
        self.session = Session()

    def create_user(self):
        username = input("Enter user's name: ")
        user = User(username=username)
        self.session.add(user)
        self.session.commit()
        print(f"User {username} created!")
        input("Press Enter to return to the main menu...")