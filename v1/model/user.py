import random

class user(object):

	def __init__(self,username,password,email, phone_number =  None, location = None, activated = False,Id = None):
		self.username = username
		self.password = password
		self.email = email
		self.phone_number = phone_number
		self.location = location
		self.activated = activated
		self.id = Id
		if Id == None:
			self.id = self.randomDigits(512)


	def get_name(self):
		return self.username

	def get_password(self):
		return self.password

	def get_email(self):
		return self.email

	def get_phone_number(self):
		return self.phone_number

	def get_location(self):
		return self.location

	def get_activated(self):
		return self.activated

	def set_name(self, username):
		self.username = username

	def set_password(self, password):
		self.password = password

	def set_email(self, email):
		self.email = email

	def set_phone_number(self, phone_number):
		self.phone_number = phone_number

	def set_location(self, location):
		self.location = location

	def set_activated(self, activated):
		self.activated = activated

	def get_key(self):
		return self.email

	def randomDigits(self, digits):
		lower = 10**(digits-1)
		upper = 10**digits - 1
		return random.randint(lower, upper)

	def __str__(self):
		return "%s, %s, %s, %s, %s, %s" % (self.username,self.password,self.email ,self.phone_number,self.location,self.activated)




