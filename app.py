import csv
from flask import Flask 
from flask import render_template

app = Flask(__name__)

# Get the csv in a form the HTML can use ("our cheap database")
def get_csv():
    csv_path = 'static/la-riots-deaths.csv'
    csv_file = open(csv_path, 'rb')
    csv_obj = csv.DictReader(csv_file)		# Needed b/c Python doesn't automatically know this is a csv
    										# Program DictReader returns the rows as individual dictionaries
    										# 	e.g., [ {'id':1, 'name':'Aviva'}, {id':2, 'name':'Brad'}, {id':3, 'name':'Corey'} ]
    csv_list = list(csv_obj)				# Stores DictReader's full list of dictionaries
    										# Do not do if you're using a huge file!
    return csv_list

# Routes us to webpage
@app.route('/') 							# '/' refers to the homepage of any website
def index():
	template = "index.html"
	object_list = get_csv()					# 'object list' = list of things you're gonna do stuff with 				
	return render_template(template, object_list=object_list) # keyword arg object_list can be anything; it just corresponds to what it will be called in the template

# Create an individual 'details' page for each person, tagged by row ID 
@app.route('/<row_id>/')					
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:				# "Are you my row? Are you my row?"
            return render_template(template, object=row)

if __name__ == "__main__": 					# If this script is run from the command line...
	app.run(debug=True, use_reloader=True) 	# ...fire up the FLask test server

