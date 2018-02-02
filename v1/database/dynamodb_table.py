import table as table
import abc
import boto3
from boto3.dynamodb.conditions import Key


class dynamodb_table(table.table):
	def __init__(self,table_name,primary_key):
		self.primary_key = primary_key
		self.table_name = table_name
		self.dynamodb = boto3.resource('dynamodb')
		self.table = self.dynamodb.Table(self.table_name)

	
	def insert(self, data):
		"""Insert data into a table, return true if you were able to and false if not"""
		try:
			self.table.put_item(Item=data, ConditionExpression='attribute_not_exists('+self.primary_key+')')
			return True
		except:
			return False
		
	def get(self,key):
		try:
			response = self.table.get_item(Key = key)
		except:
			return None
		item = response['Item']
		return item

	def delete(self,key):
		try:
			response = self.table.delete_item(Key = key)
			return True
		except:
			return False

	def update(self,key,data,expected):
		#key = key of the table
		# data = {"attribute": "processing_status", "value": "completed"}
		#excepted = {"attribute": "processing_status", "value": "completed"}
		"""update data in a table, return true if you were able to and false if not"""
		try:
			update_expr = 'SET {} = :val1'.format(data['attribute'])
			response =self.table.update_item(
			Key=key,
			UpdateExpression=update_expr,
			ConditionExpression=expected["attribute"]+" = :num",
			ExpressionAttributeValues={
				':val1': data['value'],
				':num': expected["value"]
			})
			return True
		except:
			return False 

	def query(self,col,info):
		"""query a table, return info or return None """
		response = self.table.query(
			KeyConditionExpression=Key(col).eq(info)
			)
		if len(response) == 0:
			return None
		return response

