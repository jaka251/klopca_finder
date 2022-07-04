from flask import Flask, render_template, request, make_response, redirect
from tinydb import *
from tinyrecord import transaction
import json

app = Flask(__name__, template_folder='templates', static_folder='static')

# Index page
@app.route("/", methods=["POST", "GET"])
def index():
  
    
  return render_template("index.html") 


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)