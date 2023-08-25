import click
from db.models import Session, User, Note, Tag
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
from manager.user_manager import UserManager
from manager.note_manager import NoteManager


@click.group()
def cli():
    pass


users_manager = UserManager()
notes_manager = NoteManager()


notes_list = []
tags_dict = {}

@cli.command()
@click.argument("username")
def create_user(username):
    users_manager.create_user(username)
    
@cli.command()
@click.argument("username")
@click.argument("title")
@click.argument("content")
@click.option("--tags", "-t", multiple=True, help="Tags separated by commas")
def add_note(username, title, content, tags):
    notes_manager.add_note(username, title, content, tags)

@cli.command()
def show_notes():

    notes_manager.show_notes()

@cli.command()
@click.argument('note_id', type=int)
@click.argument('title')
@click.argument('content')
@click.argument('tags', nargs=-1)
def edit(note_id, title, content, tags):

    notes_manager.edit(note_id, title, content, tags)
    
    
@cli.command()
@click.argument('note_id', type=int)
def delete(note_id):
    session = Session()

    note = session.query(Note).get(note_id)
    if not note:
        click.echo('Note not found!')
        session.close()
        return
    
    session.delete(note)
    session.commit()
    session.close()

    click.echo('Note deleted successfully!')

@cli.command()
def interactive():
    """Interactive menu."""
    session = Session()

    notes = session.query(Note).all()
    

    if not notes:
        click.echo("No notes available.")
        return
    

    menu = CursesMenu("Notes", "Choose a note:")

    for note in notes:
        # menu.append_item(FunctionItem(note.title, lambda x: click.echo(note.content)))
        def display_note_content(n=note):
            click.echo(n.content)
        menu.append_item(FunctionItem(note.title, display_note_content))
    menu.show()

if __name__ == "__main__":
    cli()
