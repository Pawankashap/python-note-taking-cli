# Python Note Taking CLI App

A note-taking application with a Command-Line Interface (CLI) allows users to create, manage, and organize notes using a text-based interface within the terminal or command prompt. This type of app is ideal for users who enjoy using keyboard shortcuts and commands and prefer a distraction-free environment for note-taking. Although CLI note-taking apps offer efficient and distraction-free note-taking, they require familiarity with terminal commands. However, users who are comfortable with the command line can benefit greatly from these apps' capabilities for organization and customization.

## Project Feathers

**Text-Based Interface:** Our note-taking app is operated entirely through text-based commands entered in the terminal. With our app, you can create, edit, and delete notes using specific commands. You have the option to specify the title, content, and even tags or categories for better organization.

**Note Creation,Editing and Deleting:** With our navigation and search features, you can effortlessly locate and browse through your notes. You have the option to use commands to view a list of all your notes, access specific ones, or navigate through them using tags or categories. Additionally, our search functionality enables you to quickly find notes by entering specific keywords or phrases.


**Navigation and Search:** With our navigation and search features, you can effortlessly locate and browse through your notes. You have the option to use commands to view a list of all your notes, access specific ones, or navigate through them using tags or categories. Additionally, our search functionality enables you to quickly find notes by entering specific keywords or phrases. 

**Tagging and Categorization:** Organizing and finding related notes is made easier for users through the use of tags or categories to categorize their notes.

I hope our app simplifies your note-taking experience!

## Installation

1. Fork and clone python-note-taking-cli repo to your local machine
2. Navigate into the project directory
3. Install pipenv if you haven't already
    * pip install pipenv
4. Activate the Virtual Environment:
    If you haven't already, activate the pipenv virtual environment for your project.
    * pipenv shell
5. Install Libraries:
    Inside your virtual environment, you can install the required libraries using pipenv.
    * pip install curses-menu sqlalchemy tabulate

## Dependencies

1. **Alembic:**
Alembic is a database migration tool for SQLAlchemy, a popular Object-Relational Mapping (ORM) library in Python. Alembic allows you to manage and automate the versioning and evolution of your database schema. It helps you apply changes to your database schema over time, supporting tasks like creating new tables, modifying columns, and more, while maintaining data integrity.

2. **SQLAlchemy:**
SQLAlchemy is a powerful and flexible Object-Relational Mapping (ORM) library for Python. It provides an abstraction layer over database interactions, allowing you to work with databases using Python classes and objects. SQLAlchemy supports a wide range of database systems and offers various levels of abstraction, from raw SQL queries to high-level ORM capabilities.

3. **curses:**
The curses library is part of Python's standard library and enables the creation of text-based user interfaces within terminal environments. It provides functions for managing terminal output, cursor movement, and user input. curses allows you to create interactive applications with menus, text windows, and more, making it suitable for developing command-line tools with a graphical-like interface.

4. **ipdb:**
ipdb is an enhanced interactive debugger for Python. It's an alternative to the built-in pdb debugger and provides a more feature-rich debugging experience. ipdb allows you to set breakpoints, inspect variables, and execute code within the context of your debugging session. It's particularly useful for interactive debugging in terminal environments.


## Project Structure

* notes is the main directory
* models is file in SQLAlchemy serves as a bridge between your application's object-oriented code and the relational database.
* manager class to handle various functions and interactions within your CLI note-taking app is a good way to organize the code.

## Usage
1. **Launch the App:**

    Open your terminal and navigate to the directory where your CLI Note Taking App is located. Run the app by executing the appropriate command:
     * python notes.py.


2. **Main Menu:**

    After launching the app, you'll see the main menu displayed in the terminal. The main menu typically presents various options that you can choose from using the keyboard.

3. **Create User:**

    Choose this option to create a new user account. This function is responsible for creating a new user account within the Note Taking App. It typically involves prompting the user to provide a username and then saving this information to a database. 

4. **Add Note:**

    To add a new note, choose the "Add Note" option. The purpose of this function is to add a new note to the user's collection of notes. It involves capturing the title and content of the note from the user, associating the note with the currently logged-in user, and saving it to the database. 

5. **Edit Note:**

    If you want to edit an existing note, select the "Edit Note" option. This function allows the user to edit the content of an existing note. It typically involves presenting the user with a list of their notes, allowing them to choose a note to edit, and then updating the note's content. 

6. **Show Note:**

    Choose the "View Notes" option to see a list of all your saved notes. This function displays a list of the user's notes or shows the details of a all notes.

7. **Delete Note:**

    The purpose of this function is to delete a note that the user no longer needs. It typically involves presenting the user with a list of their notes and allowing them to choose a note to delete.

8. **Exiting the App:**

Finally, select the "Exit" option to close the app and return to your terminal prompt.

## Links
Application Link
* Python Note Taking CLI App link https://github.com/Pawankashap/python-note-taking-cli/tree/main
## Licensing
"The code in this project is licensed under MIT license."
