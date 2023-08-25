from db.models import Session, User
import click

class UserManager:
    def __init__(self):
        self.session = Session()

    def create_user(self,username):
        user = User(username=username)
        self.session.add(user)
        self.session.commit()
        print(f"User {username} created!")