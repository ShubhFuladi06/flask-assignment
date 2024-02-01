# 4. Create a Flask app with a form that accepts user input and displays it.


from flask import Flask, render_template, request
app = Flask(__name__)



# Define a route for the form page
@app.route('/')
def show_form():
    return render_template("index4.html")

@app.route("/submit_data",methods=['POST',"get" ])
def check():
    firstname = request.form.get('fname')
    lastname = request.form.get('lname')
    gend = request.form.get('gender')

    return f"The first name is {firstname} The last name is {lastname} The gender is {gend} "

if __name__ == '__main__':
    app.run(debug=True)
