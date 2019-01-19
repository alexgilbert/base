import hashlib, web
from functions import *
from user_connection import UserConnection

class Login:
    
    def GET(self):
        if logged():
            web.seeother('/')
        else:
            render = create_render()
            return render.login()

    def POST(self):
        data = web.input()
        try:
            foundUser = UserConnection.find_by_username(data.username)
            render = create_render()
            if hasattr(foundUser, "locked") and foundUser.locked == "1":
                web.ctx.session.error = "Account is Locked"
                return render.login()
            elif hasattr(foundUser, "password") and hashlib.sha256(("sAlT754-"+data.password).encode('utf-8')).hexdigest() == foundUser.password:
                print("successfull login")
                web.ctx.session.login = 1
                web.ctx.session.username = foundUser.username
                web.ctx.session.privilege = foundUser.privilege
                return web.seeother("/")
            else:
                web.ctx.session.error = "Invalid Credentials"
                return render.login()
        except Exception as e:
            print(repr(e))
            print("Error Trying to Log In")


class Reset:

    def GET(self):
        web.ctx.session.login = 0
        web.ctx.session.kill()
        raise web.seeother('/')
