from db.models import Session, User, Note, Tag
import click

class NoteManager:

    
    
    def __init__(self):
            self.session = Session()


    notes_list = []
    tags_dict = {}

    def add_note(self, username, title, content, tags):
            # session = Session()
            user = self.session.query(User).filter_by(username=username).first()
            if user:
                note = Note(title=title, content=content, user=user)
                self.session.add(note)
                # notes_list.append(self.session)
                # note1 =self. session.query(Note).first()
                # print(note1)
                # print(notes_list)
                for tag_name in tags:
                    tag = self.session.query(Tag).filter_by(name=tag_name).first()
                    if not tag:
                        tag = Tag(name=tag_name)
                    note.tags.append(tag)
                
                # session.add(notes_list)
                # # session.commit()
                # for tag_name in tags:
                #     tags_dict = session.query(Tag).filter_by(name=tag_name).first()
                #     if tag_name not in tags_dict:
                #         tags_dict[tag_name] = []
                #     tags_dict[tag_name].append(note)
                #     # note.tags.append(tags_dict)
                
            
                self.session.commit()
                # print(notes_list)
                # print (tags_dict)
                print("Note added successfully!")
            else:
                print(f"User {username} not found.")

    def show_notes(self):
    # session = Session()

        notes = self.session.query(Note).all()
        for note in notes:
            click.echo(f"ID: {note.id}, Title: {note.title}, Content: {note.content}, Tags: {', '.join(tag.name for tag in note.tags)}")
            
        self.session.close()    
    
   