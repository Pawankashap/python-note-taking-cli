from db.models import Session, User, Note, Tag
import click

class NoteManager:
    def __init__(self):
        self.session = Session()

notes_list = []
tags_dict = {}

