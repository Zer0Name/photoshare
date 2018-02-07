import dynamodb_table as dynamodb_table
from boto3.dynamodb.conditions import Key, Attr

class Users_table(dynamodb_table.dynamodb_table):
	def __init__(self,table_name,primary_key):
		super(Users_table, self).__init__(table_name,primary_key)

	def update(self,key,data,expected):
		for (k,v), (k2,v2) in zip(data.iteritems(), expected.iteritems()):
			try:
				update_expr = 'SET {} = :val1'.format(str(k))
				response =self.table.update_item(
				Key=key,
				UpdateExpression=update_expr,
				ConditionExpression=str(k2)+" = :num",
				ExpressionAttributeValues={
					':val1': str(v),
					':num': str(v2)
				})
			except:
				return False 
		return True

	def scan(self,col,data):
		response = self.table.scan(
		FilterExpression=Attr(col).eq(data)
		)
		if len(response["Items"]) == 0:
			return None
		return response["Items"]