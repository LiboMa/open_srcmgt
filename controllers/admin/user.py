import web
import model
import forms
from config.settings import *
import hashlib

session = web.config.session

class Password:

    def __init__(self):

        if session.user_id:
            self.user_id = session.user_id
        self.form = forms.Password()
    def GET(self):
        return render.password(self.form,'Reset Password')

    def POST(self):
        user = model.find_user(self.user_id)

        if self.form.validates():
            password = hashlib.md5(self.form.d.old_password).hexdigest()
            if user.password == password:
                new_password = hashlib.md5(self.form.d.new_password).hexdigest()
                model.up_passwd(self.user_id,new_password)
                return web.seeother('/')
            else:
                return render.password(self.form,'Old pasword wrong')
        else:
            return render.password(self.form,'Change Password failure!')

class Login:

    def __init__(self):
        self.form=forms.login()

    def GET(self):
        #return render.login(self.form,"Welcome to Source Management")
        return render.login()

    def POST(self):
        i = web.input()
        ### This area should use db authentication ###
        try:
            f_username=i.username.strip()
            f_password=i.password.strip()
        except ValueError:
            raise
            return None

        # Find user form database
        user = model.find_user(f_username)
        if user is None:
            #return render.login(self.form,"Welcome to Source Management", 'Username or password incorrect! Please try again...')
            return render.login('Username or password incorrect! Please try again...')
        auth = hashlib.md5(f_password).hexdigest()

        # Check authentication
        if user.password == auth:
            #web.config._session.user_id = user.username
            session.user_id = user.username
            session.user_alias = user.alias
            session.user_role = user.role
            web.setcookie('user_id', session.user_id, 3600)
            web.setcookie('user_alias', session.user_alias, 3600)
            web.setcookie('user_role', session.user_role, 3600)
            session.login = 'yes'
            return web.seeother("/")
        ### This area should use db authentication ###
        else:
            #return render.login(self.form,"Welcome to Source Management",'ooops..Password incorrect! try again...')
            return render.login('Username or Password incorrent.. try again...')

class Logout:

    def GET(self):
        session.login = 'no'
        session.user_id = None
        session._cleanup()
        session.kill()
        raise web.seeother("/")

