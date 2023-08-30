from db.models import Session, User, Note, Tag
from cursesmenu import CursesMenu
from sqlalchemy.orm import sessionmaker
from cursesmenu.items import FunctionItem
from tabulate import tabulate

class NoteManager:

    def __init__(self):
            self.session = Session()

    def add_note(self):
            notes_list = []
            tags_dict = {}
            username = input("Enter User Name: ")
            title = input("Enter Note Title: ")
            content = input("Enter Note Content: ")
            tags = input("Enter Tag: ")
            
            if not username:
                print("User name cannot be empty. Please try again.")
            elif not title:
                print("Title cannot be empty. Please try again.")
            elif not content:
                print("Content cannot be empty. Please try again.")
            else:
                user = self.session.query(User).filter_by(username=username).first()
                if user:
                    note = Note(title=title, content=content, user=user)
                    self.session.add(note)
                    notes_list.append(self.session)
                    tag_names = tags.split(',')
                    for tag_name in tag_names:  # Iterate over the tag names, not the original 'tags' string
                        tag = self.session.query(Tag).filter_by(name=tag_name).first()
                        if not tag:
                            tag = Tag(name=tag_name)
                        note.tags.append(tag)
                        tags_dict[tag_name] = note
                    self.session.commit()
                    print(f"Note added successfully!")
                else:
                    print(f"User {username} not found.")
            input("Press Enter to return to the main menu...")

    def show_notes(self):
        session = Session()
        query = session.query(Note, User.username) \
            .join(User, Note.user_id == User.id)

        results = query.all()
        records_data = []
        for note, username in results:
            tags_string =', '.join(tag.name for tag in note.tags)
            records_data.append((note.id,username, note.title, note.content, tags_string))
        
        headers = ["ID", "User Name", "Title", "Content", "Tags"]
        table = tabulate(records_data, headers=headers, tablefmt="grid")
        print(table)

        self.session.close()    
        input("Press Enter to return to the main menu...")

    def edit(self):

        note_id = input("Enter Note ID: ")
        title = input("Enter Note Title: ")
        content = input("Enter Note Content: ")
        tags = input("Enter Tag: ")

        if not note_id:
                print("Note ID cannot be empty. Please try again.")
        elif not title:
                print("Title cannot be empty. Please try again.")
        elif not content:
                print("Content cannot be empty. Please try again.")
        else:
            note = self.session.query(Note).get(note_id)
            if not note:
                print('Note not found!')
                self.session.close()
                return
            note.title = title
            note.content = content
            note.tags.clear()
            tag_names = tags.split(',')
            for tag_name in tag_names:
                tag = self.session.query(Tag).filter_by(name=tag_name.strip()).first()
                if not tag:
                    tag = Tag(name=tag_name.strip())
                note.tags.append(tag)
                
            self.session.commit()
            self.session.close()

            print('Note edited successfully!')
        input("Press Enter to return to the main menu...")

    def delete(self):
        note_id = input("Enter Note ID: ")
        if not note_id:
                print("Note ID cannot be empty. Please try again.")
        else:
            note = self.session.query(Note).get(note_id)
            if not note:
                print('Note not found!')
                self.session.close()
                return
            
            self.session.delete(note)
            self.session.commit()
            self.session.close()
 
            print('Note deleted successfully!')
        input("Press Enter to return to the main menu...")

    def interactive(self):
        notes = self.session.query(Note).all()
        if not notes:
            print("No notes available.")
            return
        menu = CursesMenu("Notes", "Choose a note:")
        for note in notes:
            def display_note_content(n=note):
                print(n.content)
            menu.append_item(FunctionItem(note.title, display_note_content))
        menu.show()
