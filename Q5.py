# 5. Implement user sessions in a Flask app to store and display user-specific data.

from flask import Flask , request,jsonify , render_template
app = Flask(__name__)

@app.route("/")
def show_form():
    return render_template('index5.html')

@app.route("/process_form",methods = ['POST'])
def check_password():
   name =  request.form.get('username')
   password = request.form.get('password')
   print({name} , {password})
   return "username and password received"



if __name__ == "__main__":
   app.run(host="0.0.0.0",port=8000) 