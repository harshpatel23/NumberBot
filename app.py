from flask import request,Flask,jsonify,make_response
import json
import requests


app = Flask(__name__)


@app.route('/',methods=['GET'])
def get():
	return "Hello"


@app.route('/',methods=['POST'])
def post():
	url="http://numbersapi.com/"
	req = request.get_json(silent=True,force=True)
	intent_name = req['queryResult']['intent']['displayName']
	if intent_name == 'numbers':
		types = req['queryResult']['parameters']['type'][0]
		number = req['queryResult']['parameters']['number']
		final_url = url+str(int(number))+'/'+str(types)+'?json'
		json_resp = requests.get(final_url)
		dict_resp = json_resp.json()
		print(dict_resp)
		text_resp = dict_resp["text"]
		return jsonify({'fulfillmentText' : text_resp})

if(__name__ =="__main__"):
	app.run(debug=True)
