import dynamodb_table as dynamodb_table

class User_event_table(dynamodb_table.dynamodb_table):
	def __init__(self,table_name,primary_key,secondary_key):
		super(User_event_table, self).__init__(table_name,primary_key)