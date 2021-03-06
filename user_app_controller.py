import hashlib
from functions import *
from user_connection import UserConnection
from app_connection import AppConnection
from user_app_connection import UserAppConnection

class AddAppToUser:
    
    def GET(self, user):
        render = create_render()
        apps = AppConnection.get_apps()
        return render.add_app_to_user(user, apps)
    
    def POST(self):
        data = web.input()
        success = UserAppConnection.add_app_to_user(data.username, data.app)
        if success == "0":
            web.ctx.session.error = "App " + data.app + " unable to be added to " + data.username
            return render.add_app()
        else:
            web.ctx.session.message = "App " + data.app + " Successfully added to " + data.username
        web.ctx.session.redirected = 1
        raise web.seeother('/users_apps')
        
        
class UsersApps:
    
    def GET(self):
        render = create_render()
        users = UserConnection.get_users()
        users_apps = {}
        for user in users:
            apps = UserAppConnection.find_apps_by_username(user.username)
            users_apps[user.username] = apps
        return render.users_apps(users_apps)
    

class RemoveAppFromUser:
    
    def GET(self, username, app):
        success = UserAppConnection.remove_app_from_user(username, app)
        if success == 1:
            web.ctx.session.message = app + " Successfully Removed from " + username
        else:
            web.ctx.session.error = "Error: Unable to remove " + app + " from " + username
        web.ctx.session.redirected = 1
        raise web.seeother('/users_apps')