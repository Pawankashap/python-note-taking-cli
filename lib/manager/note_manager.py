from db.models import Session, User, Note, Tag
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
import click

class NoteManager:
   

    def __init__(self):
            self.session = Session()

    def add_note(self, username, title, content, tags):
            notes_list = []
            tags_dict = {}
            user = self.session.query(User).filter_by(username=username).first()
            if user:
                note = Note(title=title, content=content, user=user)
                self.session.add(note)
                notes_list.append(self.session)
                for tag_name in tags:
                    tag = self.session.query(Tag).filter_by(name=tag_name).first()
                    if not tag:
                        tag = Tag(name=tag_name)
                    note.tags.append(tag)
                self.session.commit()
                print("Note added successfully!")
            else:
                print(f"User {username} not found.")

    def show_notes(self):
        session = Session()
        query = session.query(Note, User.username) \
            .join(User, Note.user_id == User.id)

        results = query.all()

        for note, username in results:
            click.echo(f"ID: {note.id} , User: {username} , Title: {note.title} , Content: {note.content} , Tags: {', '.join(tag.name for tag in note.tags)}")
 
        self.session.close()    
    
    def edit(self,note_id, title, content, tags):
        note = self.session.query(Note).get(note_id)
        if not note:
            click.echo('Note not found!')
            self.session.close()
            return
        note.title = title
        note.content = content
        note.tags.clear()
        for tag_name in tags:
            tag = self.session.query(Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            note.tags.append(tag)
        
        self.session.commit()
        self.session.close()

        click.echo('Note edited successfully!')

    def delete(self,note_id):
        note = self.session.query(Note).get(note_id)
        if not note:
            click.echo('Note not found!')
            self.session.close()
            return
        
        self.session.delete(note)
        self.session.commit()
        self.session.close()

        click.echo('Note deleted successfully!')

    def interactive(self):
        notes = self.session.query(Note).all()
        if not notes:
            click.echo("No notes available.")
            return
        menu = CursesMenu("Notes", "Choose a note:")
        for note in notes:
            def display_note_content(n=note):
                click.echo(n.content)
            menu.append_item(FunctionItem(note.title, display_note_content))
        menu.show()
