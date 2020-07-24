from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect

import requests

import threading

app = Flask(__name__)

results = []

@app.route("/", methods = ["GET", "POST"])
def home():
	
	if (request.method == "GET"):
	
		return render_template("index.html")
	
	else:
		
		results.clear()
		text = request.form.get("name").lower()
		
		url = "https://rsbuddy.com/exchange/summary.json"
		
		response = requests.get(url).json()
		
		items = {}
		items = response
		
		count = 0
		entry = []
		
		for id in items:
		
			if (items[id]["name"].lower().find(text) > -1):
				count = count + 1
				entry.append(id)
				
			if (count >= 10):
				break
			
			
		threads = []
			
		for i in range (0, count):
			t = threading.Thread(target = getPrice, args = (entry[i],))
			t.start()
			threads.append(t)
		
		for thread in threads:
			thread.join()
		
		return render_template("index.html", items = results)


def getPrice(id):

	url = "https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=" + id
	
	response = requests.get(url).json()
	
	item = {}
	item = response["item"]
	
	data = []
	data.append(item["name"])
	data.append(item["current"]["price"])
	data.append(item["day30"]["change"])
	data.append(item["day90"]["change"])
	data.append(item["day180"]["change"])
	
	results.append(data)
	


if __name__ == '__main__':
	app.run(host='0.0.0.0')