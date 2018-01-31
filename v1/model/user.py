import random

class user(object):

	def __init__(self,username,password,email, phone_number =  "None", location = "None", activated = False, Id = None):
		self.Username = str(username) #string
		self.Password = str(password) #string
		self.Email = str(email) #string
		self.Phone_number = phone_number #string
		self.Location = location #string 
		self.Activated = activated #boolean
		self.Id = str(Id) #string
		if Id == None:
			self.Id = str(self.randomDigits(512)) #string


	def get_username(self):
		return self.Username

	def get_password(self):
		return self.Password

	def get_email(self):
		return self.Email

	def get_phone_number(self):
		return self.Phone_number

	def get_location(self):
		return self.Location

	def get_activated(self):
		return self.Activated

	def get_id(self):
		return self.Id

	def set_name(self, username):
		self.Username = username

	def set_password(self, password):
		self.Password = password

	def set_email(self, email):
		self.Email = email

	def set_phone_number(self, phone_number):
		self.Phone_number = phone_number

	def set_location(self, location):
		self.Location = location

	def set_activated(self, activated):
		self.Activated = activated

	def get_key(self):
		return self.Email

	def randomDigits(self, digits):
		lower = 10**(digits-1)
		upper = 10**digits - 1
		return random.randint(lower, upper)

	def dict(self):
		data = {}
		data["Username"] = self.get_username()
		data["Email"] = self.get_email()
		data["Password"] = self.get_password()
		data["Phone-number"] = self.get_phone_number()
		data["Id"] = self.get_id()
		data["Activated"] = self.get_activated()
		data["Location"] = self.get_location()
		return data


	def __str__(self):
		return "%s, %s, %s, %s, %s, %s" % (self.username,self.password,self.email ,self.phone_number,self.location,self.activated)




