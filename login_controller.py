import hashlib, web
from functions import *
from user_connection import UserConnection

class Login:
    
    def GET(self):
        if logged():
            web.seeother('/')
        else:
            render = create_render(web.config._session.get('privilege'))
            return render.login()

    def POST(self):
        data = web.input()
        try:
            foundUser = UserConnection.find_by_username(data.username)
            if foundUser.locked == "1":
                web.config._session.error = "Account is Locked"
                render = create_render(web.config._session.get('privilege'))
                return render.login()
            elif hashlib.sha256(("sAlT754-"+data.password).encode('utf-8')).hexdigest() == foundUser.password:
                web.config._session.login = 1
                web.config._session.username = foundUser.username
                web.config._session.privilege = foundUser.privilege
                render = create_render(web.config._session.get('privilege'))
                raise web.seeother('/')
            else:
                web.config._session.error = "Invalid Credentials"
                render = create_render(web.config._session.get('privilege'))
                return render.login()
        except Exception as e:
            print(e)
            print("Error Trying to Log In")


class Reset:

    def GET(self):
        web.config._session.login = 0
        web.config._session.kill()
        raise web.seeother('/')
