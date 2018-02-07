import dynamodb_table as dynamodb_table

class Event_lookup_table(dynamodb_table.dynamodb_table):
	def __init__(self,table_name,primary_key):
		super(Event_lookup_table, self).__init__(table_name,primary_key)
