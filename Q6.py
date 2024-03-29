from distutils.log import debug 
from fileinput import filename 
from flask import *
app = Flask(__name__) 

@app.route('/') 
def main(): 
	return render_template("index6.html") 

@app.route('/success', methods = ['POST']) 
def success(): 
	if request.method == 'POST': 
		f = request.files['file'] 
		f.save(f.filename) 
		return render_template("index6_1.html", name = f.filename) 

if __name__ == "__main__":
   app.run(host="0.0.0.0",port=8000) 
