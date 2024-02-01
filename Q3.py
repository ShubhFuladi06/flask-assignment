# 3. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index2.html')

# Define a route with a dynamic parameter
@app.route('/user/<int:age>')
def show_user_profile(age):
    # This function takes the username as a parameter and renders a template with dynamic content
    return render_template('index3.html', age1=age)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5004,debug=True)