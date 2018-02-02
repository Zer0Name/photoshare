import boto3
import random
import v1.database.user_event_table as usr_evt_table
from flask import Flask, jsonify, Blueprint, request, json
from boto3.dynamodb.conditions import Key

accnt = Blueprint('account', __name__)

def ERROR(error_code,discription):
	return jsonify({
					"Success" : False,
					"Status code" : error_code,
					"Description" : discription
					})

evnt = Blueprint('evnt', __name__)

@evnt.route('/get-user-event-list', methods=['POST'])
def index():

	if not request.is_json:
		return ERROR(-1,"Request was not in the form of a json")

	# store info in memory
	content = request.get_json() 

	# check to see that only 3 inputs are given 
	if len(content) != 1:
		return ERROR(-1,"To many or to little argument given")

	#check to confirm that the correct attributes are present 
	if content.get('Id') == None:
		return ERROR(-1,"Dont have correct argument present")

	user_event = usr_evt_table.User_event_table("user_event","Id","Event_id")

	response = user_event.query(str(content["Id"]))
	if response == None:

		return jsonify(	{"Success" : "True", "Items" : {} })

	events = []
	for item in response:
		events.append({"Event_id" : str(item["Event_id"]) ,  "Event_name" : str(item["Event_name"])})


	return jsonify(	{"Success" : "True", "Items" : events  })  