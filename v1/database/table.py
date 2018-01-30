import abc

class table(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def insert(self, input):
		"""Retrieve data from the input source and return an object."""
		return
	@abc.abstractmethod
	def update(self,input):
		return 
	@abc.abstractmethod
	def query(self,row,input):
		return
	@abc.abstractmethod
	def delete(self,input):
		
	@abc.abstractmethod
	def scan(self,input):
		return




