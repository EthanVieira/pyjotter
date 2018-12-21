import sys
from notebook import Notebook, Note

class Menu:
    '''Main menu that displays user options.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                "1": self.show_notes,
                "2": self.search_notes,
                "3": self.add_note,
                "4": self.edit_note,
                "5": self.quit
                }

    def display_menu(self):
        print("""
        ---------------
        Light Book Menu
        ---------------

        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Edit Note
        5. Quit
        """)

    def run(self):
        """Menu display and takes user's input"""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print ("{0}: {1}\n{2}".format (note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a note: ")
        self.notebook.new_note(memo)
        print("New note has been added.")

    def edit_note(self):
        id = input("Enter a node id: ")
        memo = input("Enter the new modified note: ")
        tags = input("Enter the new modified tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Quitting Light Book...")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
