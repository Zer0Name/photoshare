from flask import Flask, jsonify, Blueprint,request,json
import boto3
from v1.account import accnt
from v1.event import evnt



app = Flask(__name__)
app.register_blueprint(accnt,url_prefix='/v1/account')
app.register_blueprint(evnt,url_prefix='/v1/event')

@app.route('/v1/test', methods=['GET'])
def index():
	return jsonify(	{ "Success" : "True"}) 

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Success" : "True" , 
    				'Description': "Error 404"
    				}) , 404


if __name__ == '__main__':
    app.run(debug=True)