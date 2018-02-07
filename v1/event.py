import boto3
import random
import v1.database.user_event_table as usr_evt_table
import v1.database.users_table as usr_table
import v1.database.event_table as evt_table
import v1.database.event_lookup_table as evt_lookup_table
import time
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
def get_user_event_list():

	if not request.is_json:
		return ERROR(-1,"Request was not in the form of a json")

	# store info in memory
	content = request.get_json() 

	# check to see that= only 3 inputs are given 
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

@evnt.route('/create-event', methods=['POST'])
def create_event():
	#Picture_id  = Main -> all info about the event

	if not request.is_json:
		return ERROR(-1,"Request was not in the form of a json")

	# store info in memory
	content = request.get_json() 

	# check to see that= only 3 inputs are given 
	if len(content) != 2:
		return ERROR(-1,"To many or to little argument given")

	#check to confirm that the correct attributes are present 
	if content.get('Id') == None or content.get('Event_name') == None:
		return ERROR(-1,"Dont have correct argument present")

	#connect to table 
	user_table = usr_table.Users_table("users","Email")

	#create key and get user
	if user_table.scan("Id",str(content["Id"])) == None:
		return  ERROR(-1,"Error with info")

	#generate random number for Event_id
	lower = 10**(512-1)
	upper = 10**512 - 1
	num = str(random.randint(lower, upper))

	user_event = usr_evt_table.User_event_table("user_event","Id","Event_id")

	data = {}
	data["Id"] = str(content["Id"])
	data["Event_id"] = num
	data["Event_name"] = str(content["Event_name"])
	data["Admin"] = "True"

	if not user_event.insert(data):
		return ERROR(-1,"Error, could not creating event")

	event_table = evt_table.Event_table("events","Id","Event_id",)

	data_event = {}
	data_event["Event_id"] = num
	data_event["Picture_id"] = "Main"
	data_event["Time_stamp"] =  str(int(time.time()))

	if not event_table.insert(data_event):
		return ERROR(-1,"Error, could not creating event")

	event_lookup_table = evt_lookup_table.Event_lookup_table("event_lookup","Short_event_id")

	data_event_lookup = {}
	data_event_lookup["Short_event_id"] = str(num[0:10])
	data_event_lookup["Event_name"] = str(content["Event_name"])


	if not event_lookup_table.insert(data_event_lookup):
		return ERROR(-1,"Error, could not creating event1")

	return jsonify(	{"Success" : "True"})

@evnt.route('/join-event', methods=['POST'])
def join_event():
	if not request.is_json:
		return ERROR(-1,"Request was not in the form of a json")

	# store info in memory
	content = request.get_json() 

	# check to see that= only 3 inputs are given 
	if len(content) != 2:
		return ERROR(-1,"To many or to little argument given")

	#check to confirm that the correct attributes are present 
	if content.get('Id') == None or content.get('Short_event_id') == None:
		return ERROR(-1,"Dont have correct argument present")

	#connect to table 

	event_lookup_table = evt_lookup_table.Event_lookup_table("event_lookup","Short_event_id")

	data_info ={}
	data_info["Short_event_id"] = str(content["Short_event_id"])
	response = event_lookup_table.get(data_info)

	if response == None:
		return ERROR(1,"Error, group does not exists ")


	full_event_id = str(response["Event_id"])
	event_name = str(response["Event_name"])

	user_event = usr_evt_table.User_event_table("user_event","Id","Event_id")

	data = {}
	data["Id"] = str(content["Id"])
	data["Event_id"] = full_event_id
	data["Event_name"] = event_name
	data["Admin"] = "False"

	if not user_event.insert(data):
		return ERROR(-1,"Error, could not creating event")

	return jsonify(	{"Success" : "True"})




















