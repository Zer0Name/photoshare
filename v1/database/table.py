import abc

class table(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def insert(self, data):
		"""Insert data into a table, return true if you were able to and false if not"""
		return
	@abc.abstractmethod
	def update(self,key,data,predata):
		"""update data in a table, return true if you were able to and false if not"""
		return 
	@abc.abstractmethod
	def query(self,col,info):
		"""query a table, return info or return None """
		return
	@abc.abstractmethod
	def delete(self,data):
		"""delete data in a table, return true if you were able to and false if not"""
		return
	@abc.abstractmethod
	def get(self,data):
		'''gets an item from a table or returns None if key doesnt exist'''
		return 


