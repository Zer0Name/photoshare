import abc

class table(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def insert(self, data):
		"""Insert data into a table, return true if you were able to and false if not"""
		return
	@abc.abstractmethod
	def update(self,input,expected =None):
		"""update data in a table, return true if you were able to and false if not"""
		return 
	@abc.abstractmethod
	def query(self,col,info):
		"""query a table, return info or return None """
		return
	@abc.abstractmethod
	def delete(self,key):
		"""delete data in a table, return true if you were able to and false if not"""
		return
	@abc.abstractmethod
	def get(self,key):
		'''gets an item from a table or returns None if key doesnt exist'''
		return 
	@abc.abstractmethod
	def scan(self,input):
		"""return entire table or returns None on error"""
		return




