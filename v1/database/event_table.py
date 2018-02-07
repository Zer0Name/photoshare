import dynamodb_table as dynamodb_table

class Event_table(dynamodb_table.dynamodb_table):
	def __init__(self,table_name,primary_key,secondary_key):
		super(Event_table, self).__init__(table_name,primary_key)

	def query_begin_with(self,data):
		"""query a table, return info or return None """
		response = self.table.query(
			KeyConditionExpression=Key(self.primary_key).begins_with(data)
			)
		if len(response) == 0:
			return None
		return response['Items']