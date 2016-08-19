class NotesApplication(object):


	def __init__(self, author):
		self.author = author 
		self.notes = [] 


	def create(self, note_content):  
	#creates note instances. Tests for input types.

		if not note_content:
			print "No content provided"

		elif isinstance(note_content, str):
			self.notes.append(note_content)

		elif isinstance(note_content, int):
			self.notes.append(note_content)

		else:
			print "Incompatible content provided"

		return self.notes


	def list(self): 
	#prints all the contents of the list. 

		for key, value in enumerate(self.notes):
			print 'Note ID: %s' %(note_id)
			print self.notes
			print 'By Author %s' %(author)
		



	def get(self, note_id): 
	'''
	returns the note contents at a specified index
	index starts at 0. noted_id -1 is to make sure 
	user's request matches actual index.
	'''

		note = self.notes[note_id - 1]
		return note


	def search(self, search_text): 
	#returns the results of a search.

		print 'Showing results for search < %s >' %(search_text)

		for index, entries in enumerate(self.notes):
			if entries == search_text:
				print 'Note ID: %s \n %s ' %(index+1, entries) 
				print self.notes
				print 'By Author %s' %(author)
		else:
			print 'No results found'


	def delete(self, note_id): 
	#deletes an entry at a specified index.

		for entries in self.notes:
			self.notes.pop(note_id - 1)


	def edit(self, note_id, new_content): 
	#inserts new content and replaces previous content at a specified index.

		for index, entries in enumerate(self.notes):
			note_content.insert(note_id, new_content)









