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
	def delete(self,input):
		"""delete data in a table, return true if you were able to and false if not"""
		return
		
	@abc.abstractmethod
	def scan(self,input):
		"""return entire data base or returns None id error happned"""
		return




