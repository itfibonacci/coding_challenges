# In this step your goal is to create the API endpoint to be able to add a new note. For this challenge a note consists of:
# Title
# Note Content
import random
import time

class Note:
	used_ids = set()

	def __init__(self, content):
		self.content = content
		self.id = self.generate_id()
		self.time = time.time()

	def generate_id(self):
		while True:
			id = random.randint(100000000, 999999999)
			if ( id not in self.used_ids):
				self.used_ids.add(id)
				return id

class Folder:
	def __init__(self, name) -> None:
		self.name = name
		self.notes = []

	def createNote(self, content):
		note = Note(content)
		self.notes.append(note)

	def search_note(self, keyword):
		return " ".join([note.content for note in self.notes if keyword.lower() in note.content.lower()])
	
	def edit_note(self, keyword, new_note):
		found = 0
		for note in self.notes:
			if keyword.lower() in note.content.lower():
				found += 1
		
		if (found == 0 or found > 1):
			return f"Found {found} notes based on {keyword}. Not editing any."
		else:
			for note in self.notes:
				if keyword.lower() in note.content.lower():
					note.content = new_note
			return "Content of the note has been changed"
			
	def __str__(self) -> str:
			return '\n'.join([f"{note.time}: {note.content}" for note in self.notes])

my_books = Folder("books")
my_books.createNote("read japanese books")
my_books.createNote("read japanese novels")
my_books.createNote("read norwegian")
my_books.createNote("read peterson")
my_books.createNote("read kamasutra")
print(my_books)
print(my_books.search_note("JA"))

my_books.edit_note("books", "japan sucks")
print(my_books)
