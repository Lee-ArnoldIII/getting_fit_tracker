from flask import Flask, render_template, session, redirect, request, url_for, g
from user import User
from database import Database

app = Flask(__name__)

Database.initialise(database='getting_fit_tracker', user='postgres', password='Outsmart1!@', host='localhost')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


user_email = input("Please enter your email: ")
user_first_name = input("Please enter your first name: ")
user_last_name = input("Please enter your last name: ")
user_dob = input("When were you born (YYYY-MM-DD format): ")
user_gender = input("What is your gender: ")
user_height = input("How tall are you (FT.IN format i.e. 5.7): ")

# Create User 
user = User(user_email, user_first_name, user_last_name, user_dob, user_gender, user_height, None)
# Save User to DB
user.save_to_db()

# Create login functionality if needed
# user_entered_email = input('What is your email address: ')
# user.load_from_db_by_email(user_entered_email)