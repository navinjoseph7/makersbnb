import os
from flask import Flask, request, render_template,redirect,session
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.userrepository import UserRepository
from lib.space import Space
from lib.space_repository import SpaceRepository


# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'
current_user_id = 0
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
    userid = repository.validate_user(request.form['username'],request.form['password'])
    session['current_id']=userid
    if userid != "":
        
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
    #
    # session['current_id']=
    result = repository.create(user)
    session['current_id']= result
    if result!= None:
        return render_template('homepage.html')
    else:
        return redirect("/signup")
    
@app.route('/list', methods=['GET'])
def get_list_a_space():
    return render_template('list.html')

@app.route('/list', methods=['POST'])
def post_list_a_space():
    connection = get_flask_database_connection()
    space = Space(
        None,
        request.form['spaceName'],
        request.form['description'],
        request.form['pricePerNight'],
        request.form['startDate'],
        request.form['endDate'],
        session['current_id']
    )
    repository = SpaceRepository(connection)
    result = repository.create(space)
    if result == True:
        return render_template('homepage.html')
        


#@app.route('/list', methods=['GET'])
#def get_list():
    #connection = get_flask_database_connection()
    #repository = SpaceRepository(connection)
    #spaces = repository.list_all
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
