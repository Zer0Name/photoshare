import table as table
import abc
import boto3
from boto3.dynamodb.conditions import Key

class dynamodb_table(table.table):
	def __init__(self,table_name,primary_key):
		self.primary_key = primary_key
		self.table_name = table_name
		self.dynamodb = boto3.resource('dynamodb')
		self.table = dynamodb.Table(self.table_name)


	def query(self,col,info):
		"""query a table, return info or return None """
		response = self.table.query(
    		KeyConditionExpression=Key(col).eq(info)
			)
		if len(response) == 0:
			return None
		return response

	
	def insert(self, data):
		"""Insert data into a table, return true if you were able to and false if not"""
		try:
			self.table.put_item(Item=data, ConditionExpression='attribute_not_exists('+self.primary_key+')')
			return True
		except:
			return False
		

	def update(self,input,expected =None):
		"""update data in a table, return true if you were able to and false if not"""
		return 