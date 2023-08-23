import click
from db.models import Session, User, Note, Tag

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
def list_notes():
    session = Session()

    notes = session.query(Note).all()
    for note in notes:
        click.echo(f"ID: {note.id}, Title: {note.title}, Tags: {', '.join(tag.name for tag in note.tags)}")

    session.close()

if __name__ == "__main__":
    cli()
