import boto3
import v1.database.users_table as usr_table
import random
from flask import Flask, jsonify, Blueprint, request, json
from model import user
from boto3.dynamodb.conditions import Key

accnt = Blueprint('account', __name__)

def ERROR(error_code,discription):
	return jsonify({
					"Success" : False,
					"Status code" : error_code,
					"Description" : discription
					})

@accnt.route('/create-account', methods=['POST'])
def index():
	# check to see if request is in json form 
	if not request.is_json:
		return ERROR(-1,"Request was not in the form of a json")

	# store info in memory
	content = request.get_json() 

	# check to see that only 3 inputs are given 
	if len(content) != 3:
		return ERROR(-1,"To many or to little argument given")

	#check to confirm that the correct attributes are present 
	if content.get('Username') == None or content.get('Password') == None or content.get('Email') == None:
		return ERROR(-1,"Dont have correct argument present")

	#create new user 
	new_user = user.user(str(content["Username"]),str(content["Password"]),str(content["Email"].lower()))

	#try inserting in to database if returns false means email is already in used 
	user_table = usr_table.Users_table("users","Email")
	if not user_table.insert(new_user.dict()):
		return ERROR(1,"Email address already in use")

	return jsonify(	{"Success" : True , "Description" : "Account created"})  

@accnt.route('/send-access-code', methods=['POST'])
def send_access_code():
	# check to see if request is in json form 
	if not request.is_json:
		return ERROR(-1,"Request was not in the form of a json")
	# store info in memory
	content = request.get_json() 

	# check to see that only 2 inputs are given 
	if len(content) != 2:
		return ERROR(-1,"To many or to little argument given")

	if content.get('Email') == None or content.get('Phone_number') == None:
		return ERROR(-1,"Dont have correct argument present")

	#connect to table 
	user_table = usr_table.Users_table("users","Email")
	#create full phone number
	area_code = "+1"
	number = area_code + str(content["Phone_number"])
	#generate random num
	lower = 10**(6-1)
	upper = 10**6 - 1
	num = str(random.randint(lower, upper))
	#connect to server and send message to number
	key = {}
	key["Email"] = str(content["Email"])
	response = user_table.get(key)
	if response == None:
		return  ERROR(-1,"Error with info")
	#check if account is activated already
	if response["Activated"] == True:
		return ERROR(-1,"Error, account already activated")

	#create user object with current user info 
	current_user = user.user(str(response["Username"]),str(response["Password"]),str(response["Email"].lower()),
							 str(response["Phone_number"]), str(response["Location"]),str(response["Activated"]), 
							 str(response["Id"] ))

	#update user phone number
	current_user.set_phone_number(num)
	new_data,old_data = current_user.generate_change()
	#update database
	if not user_table.update(key,new_data,old_data):
		return ERROR(-1, "Error updating database")
	#send message to phone
	sns = boto3.client('sns')
	sns.publish(PhoneNumber = number, Message=num)
	return jsonify(	{"Success" : True , "Description" : "Code sent to number"}) 





