import curses
from db.models import Session, User, Note, Tag
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
from manager.user_manager import UserManager
from manager.note_manager import NoteManager
from sqlalchemy.orm import sessionmaker

users_manager = UserManager()
notes_manager = NoteManager()


notes_list = []
tags_dict = {}

def create_user():
    users_manager.create_user()
    
def add_note():
    notes_manager.add_note()

def edit_note():

    notes_manager.edit()

def show_note():

    notes_manager.show_notes()
    
def delete_note():

    notes_manager.delete()
    
def interactive():

    notes_manager.interactive()

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor

    menu = CursesMenu("Welcome CLI Note Taking App", "Select an option:")

    menu.append_item(FunctionItem("Add User", create_user))
    menu.append_item(FunctionItem("Add Note", add_note))
    menu.append_item(FunctionItem("Edit Note", edit_note))
    menu.append_item(FunctionItem("Show Note", show_note))
    menu.append_item(FunctionItem("Delete Note", delete_note))

    menu.show()    
    
if __name__ == "__main__":
    curses.wrapper(main)
