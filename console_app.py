import movie
import accounts
import user
import time
import sys
import kivy


def main():
    system = accounts.Accounts()
    # make sure that the ser enters a number (1,2)
    menu = input('Would you like to:\n 1)sign up\n 2)log in\n ')
    while menu != '1' and menu != '2':
        print('Please enter in a number,either 1 or 2!')
        menu = int(input('Would you like to:\n 1)sign up\n 2)log in\n '))
    menu = int(menu)

    print('Processing!')
    time.sleep(1.5)
    if menu == 1:
        fname = input('whats your first name: ').lower()
        time.sleep(0.5)

        lname = input('whats your second name: ').lower()
        time.sleep(0.5)

        uname = input('Whats your username: ').lower()
        while len(system.check_uname(uname)) != 0:
            print('An account with that username already exists!')
            uname = input('Enter in another username: ')
        time.sleep(0.5)

        email = input('Whats your email: ').lower()
        while len(system.check_email(email)) != 0:
            print('An account with that email alreeady exists!')
            email = input(
                'Enter in another email or enter in "x" to exit the program: ')
            if uname == 'x':
                sys.exit()
        time.sleep(0.5)

        password = input('Whats your password: ').lower()
        password_verify = input('Please verify your password: ').lower()
        while password != password_verify:
            print('Incorrect verification!')
            password_verify = input('Please re-verify your password: ').lower()

        new_user = user.User(fname, lname, uname, email, password)
        system.add_user(new_user)
        print('Congrats on signing up!')

    elif menu == 2:
        email = input('Whats your email: ').lower()
        time.sleep(0.5)

        password = input('Whats your password: ').lower()
        if len(system.authorize(email, password)) == 0:
            print("Login failed")
        else:
            print("Welcome")


if __name__ == '__main__':
    main()
# movie1 = movie.Movie('jumanji')
# print(movie1.ratings)
