import unittest

from notes_app import NotesApplication

class notes_app_test(unittest.TestCase):

	def setUp(self):
		pass


	def test_author(self):
		#Tests if an author has been set for each new note.

		self.assertIsNone(NotesApplication(), msg='You must include an author')


	def test_empty_notes(self):
		#Tests if notes input is empty. 

		self.assertIsNone(note_content, msg='Please enter a note')


	def test_empty_list(self):
		#Tests if list is empty.

		self.assertIsNone(notes, msg='You have no notes yet')


	def test_get_index_error(self):
		#Tests the search function - if user inputs index beyond the
		#length of the list. 

		if note_id  > len(self.notes):
			print 'Your search is out of bounds'


	def test_search_text(self):
		#Tests if search text matches entries in notes list.

		for index, entries in enumerate(self.notes):
			if entries != search_text:
				print '%s does not exist' %(search_text)


	def test_deleting_wrong_index(self):
		#Tests if index selected for deletion is outside the list length.

		if note_id > len(self.notes):
			print 'Your input is out of bounds'

'''
	def test_edit_content_error(self):
		#Tests to see if edited content is saved in the correct index

		for index, entries in enumerate(self.notes):
			note_content.insert(note_id, new_content)
			return self.expectedFailure()
'''


if __name__ == '__main__':
	unittest.main()