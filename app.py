import os
from flask import Flask, request, render_template,redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.userrepository import UserRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /homepage
# Returns the homepage once the user has logged in
# Has the option to book or list a space

@app.route('/homepage', methods=['GET'])
def get_homepage_once_logged_in():
    return render_template('homepage.html')

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index


@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def post_index():
    connection = get_flask_database_connection()
    repository = UserRepository(connection)
    result=repository.validate_user(request.form['username'],request.form['password'])
    if result ==True:
        return render_template('homepage.html')
    else:
        return redirect("/index")


@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    connection = get_flask_database_connection()
    user = User(
        None, 
        request.form['name'],
        request.form['email'],
        request.form['password']
    )
    repository = UserRepository(connection)
    result = repository.create(user)
    if result ==True:
        return render_template('homepage.html')
    else:
        return redirect("/signup")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
