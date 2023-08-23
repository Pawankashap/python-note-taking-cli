import click
from db.models import Session, User, Note, Tag
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem

@click.group()
def cli():
    pass

@cli.command()
@click.argument("username")
def create_user(username):
    session = Session()
    user = User(username=username)
    session.add(user)
    session.commit()
    print(f"User {username} created!")

@cli.command()
@click.argument("username")
@click.argument("title")
@click.argument("content")
# @click.argument("tags")
@click.option("--tags", "-t", multiple=True, help="Tags separated by commas")
def add_note(username, title, content, tags):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        note = Note(title=title, content=content, user=user)
        session.add(note)
        print(tags)
        print("run this section")
        for tag_name in tags:
            tag = session.query(Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            note.tags.append(tag)
        session.commit()
        print("Note added successfully!")
    else:
        print(f"User {username} not found.")

@cli.command()
def show_notes():
    session = Session()

    notes = session.query(Note).all()
    for note in notes:
        click.echo(f"ID: {note.id}, Title: {note.title}, Content: {note.content}, Tags: {', '.join(tag.name for tag in note.tags)}")

    session.close()


@cli.command()
@click.argument('note_id', type=int)
@click.argument('title')
@click.argument('content')
@click.argument('tags', nargs=-1)
def edit(note_id, title, content, tags):
    session = Session()

    note = session.query(Note).get(note_id)
    if not note:
        click.echo('Note not found!')
        session.close()
        return
    
    note.title = title
    note.content = content

    # Clear existing tags and add new ones
    note.tags.clear()
    for tag_name in tags:
        tag = session.query(Tag).filter_by(name=tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
        note.tags.append(tag)
    
    session.commit()
    session.close()

    click.echo('Note edited successfully!')



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
