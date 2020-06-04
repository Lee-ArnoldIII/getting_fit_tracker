from database import CursorFromConnectionFromPool

class User:
    # Update user to include any additional information/ data for DB
    def __init__(self, email, first_name, last_name, date_of_birth, gender, height, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.height = height
        self.id = id

    # Not sure this is needed yet, but have it just in case
    def __str__(self):
        pass

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO users (email, first_name, last_name, date_of_birth, gender, height ) VALUES (%s, %s, %s, %s, %s, %s)',
                          (self.email, self.first_name, self.last_name, self.date_of_birth, self.gender, self.height))
        

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
            user_data = cursor.fetchone()
            return cls(email=user_data[1], first_name=user_data[2],
                        last_name=user_data[3], date_of_birth=user_data[4],
                        gender=user_data[5], height=user_data[6],
                        id=user_data[0])