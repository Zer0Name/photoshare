import dynamodb_table as dynamodb_table

class Users_table(dynamodb_table.dynamodb_table):
	def __init__(self,table_name,primary_key):
		super(Users_table, self).__init__(table_name,primary_key)

	def update(self,key,data,expected):
		for (k,v), (k2,v2) in zip(data.iteritems(), expected.iteritems()):
			print k,v
			print k2,v2
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