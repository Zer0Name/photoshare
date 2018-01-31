import boto3
import v1.database.dynamodb_table as dbt
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

	new_user = user.user(str(content["Username"]),str(content["Password"]),str(content["Email"].lower()))

	#check if email is already in the system
	#try inserting in to database if returns false means email is already in used 
	user_table = dbt.dynamodb_table("users","Email")
	if not user_table.insert(new_user.dict()):
		return ERROR(1,"Email address already in use")

	return jsonify(	{"Success" : True , "Description" : "Account created"})  





    # print request.is_json
	# content = request.get_json()
	# print len(content)
	#area_code = "+1"
	# number = area_code + content["Phone-number"]
	# sns = boto3.client('sns')
	# sns.publish(PhoneNumber = number, Message='meesage to send')