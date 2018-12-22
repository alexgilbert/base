from conf.functions import *
from connection.user_connection import UserConnection
import hashlib

class addUser:
    
    def GET(self):
        render = create_render(web.config._session.get('privilege'))
        return render.registration()
    
    def POST(self):
        data = web.input()
        print(data.username)
        existingUser = UserConnection.find_by_username(username = data.username)
        render = create_render(web.config._session.get('privilege'))
        if data.confirm != data.password:
            web.config._session.error = "Passwords do not match.\n"
            return render.registration()
        elif hasattr(existingUser, 'username') and existingUser.username == data.username:
            web.config._session.error = "User already in use.\n"
            return render.registration()
        else:
            data.password = hashlib.sha256(("sAlT754-"+ data.password).encode('utf-8')).hexdigest()
            UserConnection.add(data)
            web.config._session.message = "Welcome " + data.first
            raise web.seeother('/')