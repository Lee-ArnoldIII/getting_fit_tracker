from flask import Flask, render_template, session, redirect, request, url_for, g
# from user import User
# from database import Database

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Tait', password='password'))
users.append(User(id=2, username='Lee', password='secret'))


app = Flask(__name__)
app.secret_key = 'youdontgettoknowthis'

# Database.initialise(database='getting_fit_tracker', user='postgres', password='Outsmart1!@', host='localhost')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login2.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

app.run(port=4995, debug=True)

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

