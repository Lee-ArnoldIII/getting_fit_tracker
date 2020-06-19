from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
# from user import User
# from database import Database

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Outsmart1!@@localhost/get_fit_tracker'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    date_of_birth = db.Column(db.DateTime())
    gender = db.Column(db.String(200))
    height = db.Column(db.Integer)

    def __init__(self, email, first_name, last_name, date_of_birth, gender, height):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.height = height

@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        date_of_birth = request.form['dob']
        gender = request.form['gender']
        height = request.form['height']
        print(email, first_name, last_name, date_of_birth, gender, height)
        if email == '' or 

        # Add condition checks for validation and redirect
        # Set up db query code
        # Set up app.run code








'''
All code below is previous version of connection to db. Replaced with above code.
'''

# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password

#     def __repr__(self):
#         return f'<User: {self.username}>'

# users = []
# users.append(User(id=1, username='Tait', password='password'))
# users.append(User(id=2, username='Lee', password='secret'))


# app = Flask(__name__)
# app.secret_key = 'youdontgettoknowthis'

# Database.initialise(database='getting_fit_tracker', user='postgres', password='Outsmart1!@', host='localhost')

# @app.before_request
# def before_request():
#     g.user = None

#     # if 'user_id' in session:
#     #     user = [x for x in users if x.id == session['user_id']][0]
#     #     g.user = user

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session.pop('user_id', None)
        
#         username = request.form['username']
#         password = request.form['password']

#         # user = [x for x in users if x.username == username][0]
#         # if user and user.password == password:
#         #     session['user_id'] = user.id
#         #     return redirect(url_for('profile'))

#         return redirect(url_for('login'))

#     return render_template('login.html')

# @app.route('/registration')
# def registration():
#     return render_template('registration.html')

# @app.route('/profile')
# def profile():
#     if not g.user:
#         return redirect(url_for('login'))
        
#     return render_template('dashboard.html')



# app.run(port=4995, debug=True)

# user_email = input("Please enter your email: ")
# user_first_name = input("Please enter your first name: ")
# user_last_name = input("Please enter your last name: ")
# user_dob = input("When were you born (YYYY-MM-DD format): ")
# user_gender = input("What is your gender: ")
# user_height = input("How tall are you (FT.IN format i.e. 5.7): ")

# Create User 
# user = User(user_email, user_first_name, user_last_name, user_dob, user_gender, user_height, None)
# Save User to DB
# user.save_to_db()

# Create login functionality if needed
# user_entered_email = input('What is your email address: ')
# user.load_from_db_by_email(user_entered_email)

