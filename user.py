class User:

    firstName = None
    lastName = None
    username = None
    email = None
    password = None

    def __init__(self, fname, lname, uname, email, password):
        self.firstName=fname
        self.lastName=lname
        self.username=uname
        self.email=email
        self.password=password
