import sqlite3
import user


class Accounts:

    users = []
    conn = sqlite3.connect('user.db')
    c = conn.cursor()

    def __init__(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS testing (
            firstName text,
            lastName text,
            userName text,
            email text,
            password text
            )""")

    def add_user(self, user):
        self.c.execute("INSERT INTO testing VALUES (?,?,?,?,?)",
                       (user.firstName, user.lastName, user.username, user.email, user.password))

        self.conn.commit()

    def check_email(self, value):
        self.c.execute("SELECT rowid FROM testing WHERE email=?", (value,))
        db_result_email = self.c.fetchall()
        return db_result_email

    def check_uname(self, value):
        self.c.execute("SELECT rowid FROM testing WHERE username=?",
                       (value,))
        db_result_uname = self.c.fetchall()
        return db_result_uname

    def authorize(self, email, password):
        statement = f"SELECT rowid FROM testing WHERE email='{email}' AND password = '{password}';"
        self.c.execute(statement)
        db_result_auth = self.c.fetchall()
        return db_result_auth
        # An empty result evaluates to False.
        #    return "Login failed"
        # else:
        #    return "Welcome"
