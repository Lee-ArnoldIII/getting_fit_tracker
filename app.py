from flask import Flask, render_template, redirect, request, url_for, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = '1234'
ENV = 'prod'
# ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Outsmart1!@@localhost/getting_fit_tracker'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uxtdeekazwvzvh:4cec2432430dd3c9bd0035b438b7c95ca84a04bc8543924bcf18ae8ec3276ba9@ec2-52-72-65-76.compute-1.amazonaws.com:5432/dbd00ki5fp792n'

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
    workouts = db.relationship('Workouts', backref='user', lazy=True)

    def __init__(self, username, email, password, first_name, last_name, gender, height):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.height = height

class Workouts(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    workout_type = db.Column(db.String(200))
    workout_length = db.Column(db.String(200))
    item = db.Column(db.String(200))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, workout_type, workout_length, item, users_id):
        self.workout_type = workout_type
        self.workout_length = workout_length
        self.item = item
        self.users_id = users_id
    


# @app.before_request
# def before_request():
#     g.user = None

    # if 'user_id' in session:
    #     user = [x for x in users if x.id == session['user_id']][0]
    #     g.user = user

    #     if request.method == 'POST':
#         session.pop('user_id', None)
        
#         username = request.form['username']
#         password = request.form['password']

#         # user = [x for x in users if x.username == username][0]
#         # if user and user.password == password:
#         #     session['user_id'] = user.id
#         #     return redirect(url_for('profile'))

#         return redirect(url_for('login'))
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
                session['username'] = username 
                print(session['username'])
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

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session:
        if session['username']:
            return render_template('dashboard.html')
        return render_template('login.html', message='Please log in')
    return render_template('login.html', message='You Must Log In to Use Dashboard')


@app.route('/workout_log', methods=['GET', 'POST'])
def workouts():
    if session:
        if session['username']:
            return render_template('workout_log.html')
    return render_template('login.html', message='Please log in')
    
    if request.method == 'POST':
        workout_type = request.form['workout_type']
        workout_length = request.form['workout_length']
        item = request.form['item']
        users_id = None

        if workout_type == '' or workout_length == '' or item == '':
            return render_template('workout_log.html', message='Please enter required fields')
        if User.query.filter_by(username=session['username']).count() == 1:
            users_id = User.query.filter_by(username=session['username']).first()
            print('There is a user')
            print(users_id.id)
            data = Workouts(workout_type, workout_length, item, users_id.id)
            db.session.add(data)
            db.session.commit()
            return render_template('workout_log.html', message='Workout logged successfuly!')
    return render_template('workout_log.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return render_template('login.html', message='You have been logged out')

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






