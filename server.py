from flask import Flask 

app = Flask(__name__)

app.secret_key = "Supermegasecret"



if name == "main":
	app.run(port=5000, host='0.0.0.0')