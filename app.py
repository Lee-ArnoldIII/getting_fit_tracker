from user import User
from database import Database

Database.initialise(database='getting_fit_tracker', user='postgres', password='Outsmart1!@', host='localhost')

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