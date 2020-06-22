from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
# from user import User
# from database import Database

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Outsmart1!@@localhost/getting_fit_tracker'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    height = db.Column(db.Integer)

    def __init__(self, username, email, password, first_name, last_name, gender, height):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.height = height


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == '' or password == '':
            return render_template('login.html', message='Please enter requied fields')
        if User.query.filter_by(username=username).all():
            if User.query.filter_by(password=password).all():
                return redirect(url_for('dashboard'))
            return render_template('login.html', message='Username/Password does not match')
        return render_template('login.html', message='User does not exist')
    return render_template('login.html')

@app.route('/registration', methods=['GET'])
def registration():
    return render_template('registration.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        gender = request.form['gender']
        height = request.form['height']
               
        print(email, first_name, last_name, gender, height, username, password)
        if email == '' or username == '':
            return render_template('registration.html', message='Please enter required fields')
        if db.session.query(User).filter(User.username == username).count() == 0:
            data = User(username, email, password, first_name, last_name, gender, height)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        return render_template('registration.html', message='An account with that information already exists')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/workout_log', methods=['GET', 'POST'])
def workout_log():
    return render_template('workout_log.html')

if __name__ == '__main__':
    app.run()


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

