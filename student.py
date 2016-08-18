from datetime import datetime

class Student(object): #object allows for inheritance
		

	map_ = {
	'KE':'Kenya',
	'UG':'Uganda',
	'TZ':'Tanzania',
	'NG':'Nigeria'
	}

	student_attendance = {}

	id_holder = 0

	

	def __init__(self, id, fname, lname, country='KE'): #a function within a class is a method
		self.id = id_holder 
		self.fname = fname
		self.lname = lname
		self.country = Student.map_[country]
		
		id_holder += 1


	def attend_class(self, **kwargs):
		loc = kwargs.get('loc', 'Hogwarts')
        date = kwargs.get('date', datetime.today())
        teacher = kwargs.get('teacher', 'Alex')

        if date in Student.student_attendance.keys():
        	Student.student_attendance[date].append(self.fname)

        else: 
        	Student.student_attendance[date].append(self.fname)

        #set default values for location, date and teacher. 
        #then use the empty student attendance dictionary to store 
        # and match student names to dates.  
        
    	@staticmethod    
    	def get_attendance(date):
    			if date in Student.attended_students.keys():
    				print(Student.attend_students[date])

    			else:
    				print('None')

    	#@staticmethod is class method. Here if a date is present, 
    	#we print the name (value) associated with that date (key).


