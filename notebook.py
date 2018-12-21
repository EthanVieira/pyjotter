import datetime

# The next id for new notes. This gives each note a unique identifier.
last_id = 0

class Notebook:
    '''A collection of notes that can be editted and searched.'''

    def __init__(self):
        '''The notebook shall initially be an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Write a new note (memo) and save it to the notebook.'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, id):
        '''Finds any saved note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(id):
                return note
        return None

    def edit_memo(self, id, memo):
        '''Changes the memo to the given value for any note with the given id.'''
        note = self._find_note(id)
        if note:
            note.memo = memo
            return True
        return False

    def edit_tags(self, id, tags):
        '''Changes the space-separated tags to the given value(s) for any note with the given id.'''
        self._find_note(id).tags = tags

    def search(self, filter):
        '''Searches all of the notes for any that match the given string.'''
        return [note for note in self.notes if note.match(filter)]

class Note:
    '''A note in the notebook.'''

    def __init__(self, memo, tags=''):
        '''A note with memo and optional space-separated tags to help find notes in potential queries.
        The creation date and note id are automatically created.'''
        self.memo = memo
        self.tags = tags
        self.init_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Compare ths note to filter text to determine whether or not they matchself.
        This works for both text and tags.'''
        return filter in self.memo or filter in self.tags
