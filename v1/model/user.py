import random

class user(object):

	def __init__(self,username,password,email, phone_number =  "None", activated = "False", Id = None):
		self.Username = str(username) #string
		self.Password = str(password) #string
		self.Email = str(email) #string
		self.Phone_number = str(phone_number) #string
		self.Activated = str(activated) #boolean
		self.Id = str(Id) #string
		if Id == None:
			self.Id = str(self.randomDigits(512))
		self.old_info = None



	def get_username(self):
		return self.Username


	def get_password(self):
		return self.Password

	def get_email(self):
		return self.Email

	def get_phone_number(self):
		return self.Phone_number

	def get_activated(self):
		return self.Activated

	def get_id(self):
		return self.Id

	def set_name(self, username):
		if self.old_info == None:
			self.old_info = user(self.Username,self.Password,self.Email,self.Phone_number,self.Location,self.Activated,self.Id)
		self.Username = str(username)

	def set_password(self, password):
		if self.old_info == None:
			self.old_info = user(self.Username,self.Password,self.Email,self.Phone_number,self.Location,self.Activated,self.Id)
		self.Password = str(password)

	def set_email(self, email):
		if self.old_info == None:
			self.old_info = user(self.Username,self.Password,self.Email,self.Phone_number,self.Location,self.Activated,self.Id)
		self.Email = str(email)

	def set_phone_number(self, phone_number):
		if self.old_info == None:
			self.old_info = user(self.Username,self.Password,self.Email,self.Phone_number,self.Location,self.Activated,self.Id)
		self.Phone_number = str(phone_number)

	def set_activated(self, activated):
		if self.old_info == None:
			self.old_info = user(self.Username,self.Password,self.Email,self.Phone_number,self.Location,self.Activated,self.Id)
		self.Activated = str(activated)

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
		data["Phone_number"] = self.get_phone_number()
		data["Id"] = self.get_id()
		data["Activated"] = self.get_activated()
		return data

	#returns None if no changes has been made
	def generate_change(self):
		if self.old_info == None:
			return None
		data_new = {}
		data_old = {} 
		for (k,v), (k2,v2) in zip(self.__dict__.iteritems(), self.old_info.__dict__.iteritems()):
			if k == k2 and v != v2 and k != 'old_info':
				data_new[k] =  v
				data_old[k2] = v2
		if len(data_new) == 0:
			return None
		return data_new,data_old
			

	def __str__(self):
		return "%s, %s, %s, %s, %s, %s" % (self.Username,self.Password,self.Email ,self.Phone_number,self.Activated)




