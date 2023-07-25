from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import accounts
import user
import movie

system = accounts.Accounts()


class LogIn(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        email = self.email.text
        password = self.password.text
        if len(system.authorize(email, password)) == 0:
            self.password.text = ''
            return "Login failed"
        else:
            return "Welcome"


class SignUp(Screen):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    uname = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def enter(self):
        fname = self.fname.text
        lname = self.lname.text
        uname = self.uname.text
        email = self.email.text
        password = self.password.text
        if len(system.check_uname(uname)) != 0:
            print('An account with that username already exists!')
            self.uname.text = ''
            return 'failed'
        elif len(system.check_email(email)) != 0:
            print('An account with that email alreeady exists!')
            self.email.text = ''
            return 'failed'
        else:
            new_user = user.User(fname, lname, uname, email, password)
            system.add_user(new_user)
            print('Congrats on signing up!')
            return 'Welcome'


class Main(Screen):

    def displayImg(self):
        pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('UI.kv')


class UI(App):
    def build(self):
        return kv


if __name__ == '__main__':
    UI().run()
