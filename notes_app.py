class NotesApplication(object):

	#note_id = 0
	#master_l = {} #to take kay:value of author:content

	def __init__(self, author):
		self.author = author 
		self.notes = [] 


	def create(self, note_content):
		if not note_content:
			print "No content provided"

		elif isinstance(note_content, str):
			self.notes.append(note_content)

		elif isinstance(note_content, int):
			self.notes.append(note_content)

		else:
			print "Incompatible content provided"


	def list(self):
		
		print 'Note ID: %s' %(note_id)
		print self.notes
		print 'By Author %s' %(author)

		pass

	def get(self, note_id):
		note = self.notes[note_id - 1]
		#return str(note_id)

		#NotesApplication.note_id += 1
		
		
		#master_l.append(notes)

	def search(self, search_text):
		print 'Showing results for search < %s >' %(search_text)

		for index, entries in enumerate(self.notes):
			if entries == search_text:
				print 'Note ID: %s \n %s ' %(index+1, entries) 
				print 'By Author %s' %(author)
		else:
			print 'No results found'


test = NotesApplication('MLK')
test = NotesApplication('Poe')
test.create('I have a dream')
test.create('Something about crows')
print test.create
test.search('MLK')
test.get(1)
print test.search("")





