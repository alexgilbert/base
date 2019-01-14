import hashlib
from functions import *
from user_connection import UserConnection

class addUser:
    
    def GET(self):
        render = create_render(web.config._session.get('privilege'))
        return render.registration()
    
    def POST(self):
        data = web.input()
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
            web.config._session.redirected = 1
            raise web.seeother('/')
        
        
class Users:
    
    def GET(self):
        render = create_render(web.config._session.get('privilege'))
        users = UserConnection.get_users()
        return render.users(users)
    

class EditUser:
    
    def GET(self, username):
        render = create_render(web.config._session.get('privilege'))
        existingUser = UserConnection.find_by_username(username)
        if hasattr(existingUser, 'username'):
            return render.edit_user(existingUser)
        else:
            web.config._session.error = "Unable to find " + username;
            web.config._session.redirected = 1
            raise web.seeother('/users')
     
     
class UpdateUser:
    
    def POST(self):
        data = web.input()
        error = 0
        if data.password != data.confirm:
            web.config._session.error = "Passwords must match"
            error = 1
        if data.existing != data.username:
            newUserFound = UserConnection.find_by_username(data.username)
            if hasattr(newUserFound, "username"):
                web.config._session.error = "New Username already in use"
                error = 1
        web.config._session.redirected = 1
        if error == 0:
            data.password = hashlib.sha256(("sAlT754-"+ data.password).encode('utf-8')).hexdigest()
            success = UserConnection.update(data)
            if success == 1:
                web.config._session.message = "User successfully updated"
            else:
                web.config._session.error = "Error in updating user"
            raise web.seeother('/users')
        else:
            raise web.seeother('/edit_user/'+data.existing)            

class DeleteUser:
    
    def GET(self, username):
        success = UserConnection.del_by_username(username)
        if success == 1:
            web.config._session.message = username + " Successfully Deleted"
        else:
            web.config._session.error = "Error: Unable to delete " + username
        web.config._session.redirected = 1
        raise web.seeother('/users')
    

class LockUser:
    
    def GET(self, username):
        success = UserConnection.lock_by_username(username)
        if success == 1:
            web.config._session.message = username + " Successfully Locked"
        else:
            web.config._session.error = "Error: Unable to lock " + username
        web.config._session.redirected = 1
        raise web.seeother('/users')


class UnlockUser:
    
    def GET(self, username):
        success = UserConnection.unlock_by_username(username)
        if success == 1:
            web.config._session.message = username + " Successfully Unlocked"
        else:
            web.config._session.error = "Error: Unable to unlock " + username
        web.config._session.redirected = 1
        raise web.seeother('/users')