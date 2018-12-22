import hashlib, web
from conf.functions import *
from connection.user_connection import UserConnection

class Login:
    
    def GET(self):
        if logged():
            web.redirect('/')
        else:
            render = create_render(web.config._session.get('privilege'))
            return render.login()

    def POST(self):
        data = web.input()
        try:
            foundUser = UserConnection.findByUsername(data.username)
            if hashlib.sha256(("sAlT754-"+data.password).encode('utf-8')).hexdigest() == foundUser.password:
                web.config._session.login = 1
                web.config._session.username = foundUser.username
                web.config._session.privilege = foundUser.privilege
                render = create_render(web.config._session.get('privilege'))
                raise web.seeother('/')                
        except:
            print("Error Trying to Log In")
        
        web.config._session.login = 0
        web.config._session.privilege = 0
        web.config._session.username = "Guest"
        web.config._session.error = "Invalid Credentials"
        render = create_render(web.config._session.get('privilege'))
        return render.login()


class Reset:

    def GET(self):
        web.config._session.login = 0
        web.config._session.kill()
        raise web.seeother('/')
