from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/') 							# '/' refers to the homepage of any website
def index():
	template = "index.html"
	return render_template(template)

if __name__ == "__main__": 					# If this script is run from the command line...
	app.run(debug=True, use_reloader=True) 	# ...fire up the FLask test server

