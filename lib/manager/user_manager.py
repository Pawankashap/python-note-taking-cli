from db.models import Session, User

class UserManager:
    def __init__(self):
        self.session = Session()

    def create_user(self):
        username = input("Enter user's name: ")
        if not username:
            print("User name cannot be empty. Please try again.")
        else:
            user = User(username=username)
            self.session.add(user)
            self.session.commit()
            print(f"User {username} created!")
        input("Press Enter to return to the main menu...")