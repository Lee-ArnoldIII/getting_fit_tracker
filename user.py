class User:
    # Update user to include any additional information/ data for DB
    def __init__(self, email, first_name, last_name, date_of_birth, gender, height):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.height = height

    # Not sure this is needed yet, but have it just in case
    def __str__(self):
        pass

    