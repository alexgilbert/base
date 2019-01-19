import hashlib
from functions import *
from user_connection import UserConnection
from app_connection import AppConnection
from user_app_connection import UserAppConnection

class AddApp:
    
    def GET(self):
        render = create_render()
        return render.add_app()
    
    def POST(self):
        data = web.input()
        existingApp = AppConnection.find_by_name(name = data.name)
        existingUrl = AppConnection.find_by_url(url = data.url)
        render = create_render()
        if hasattr(existingApp, 'name'):
            web.ctx.session.error = "App name already in use.\n"
            return render.add_app()
        elif hasattr(existingUrl, 'name'):
            web.ctx.session.error = "App Url already in use.\n"
            return render.add_app()
        else:
            AppConnection.add(data)
            web.ctx.session.message = "App " + data.name + "Successfully Created"
            web.ctx.session.redirected = 1
            raise web.seeother('/apps')
        
        
class Apps:
    
    def GET(self):
        render = create_render()
        apps = AppConnection.get_apps()
        return render.apps(apps)
    

class EditApp:
    
    def GET(self, name):
        render = create_render()
        existingApp = AppConnection.find_by_name(name)
        if hasattr(existingApp, 'name'):
            return render.edit_app(existingApp)
        else:
            web.ctx.session.error = "Unable to find " + name;
            web.ctx.session.redirected = 1
            raise web.seeother('/apps')
     
     
class UpdateApp:
    
    def POST(self):
        data = web.input()
        error = 0
        if data.existing != data.name:
            newAppFound = AppConnection.find_by_name(data.name)
            if hasattr(newAppFound, "name"):
                web.ctx.session.error = "New App Name already in use"
                error = 1
        newUrlFound = AppConnection.find_by_url(data.url)
        if hasattr(newUrlFound, "name") and newUrlFound.name != data.existing:
                web.ctx.session.error = "New App URL already in use"
                error = 1         
        web.config.session_parameters['redirected'] = 1
        if error == 0:
            success = AppConnection.update(data)
            if success == 1:
                web.message = "App successfully updated"
            else:
                web.error = "Error in updating app"
            raise web.seeother('/apps')
        else:
            raise web.seeother('/edit_app/'+data.existing)            

class DeleteApp:
    
    def GET(self, name):
        success = AppConnection.del_by_name(name)
        users = UserConnection.get_users()
        for user in users:
            UserAppConnection.remove_app_from_user(user.username,name)
        if success == 1:
            web.message = name + " Successfully Deleted"
        else:
            web.error = "Error: Unable to delete " + name
        web.redirected = 1
        raise web.seeother('/apps')
    

class DeactivateApp:
    
    def GET(self, name):
        success = AppConnection.deactivate_by_name(name)
        users = UserConnection.get_users()
        for user in users:
            UserAppConnection.remove_app_from_user(user.username,name)
        if success == 1:
            web.message = name + " Successfully Deactivated"
        else:
            web.error = "Error: Unable to deactivate " + name
        web.redirected = 1
        raise web.seeother('/apps')


class ActivateApp:
    
    def GET(self, name):
        success = AppConnection.activate_by_name(name)
        if success == 1:
            web.message = name + " Successfully Activated"
        else:
            web.error = "Error: Unable to activate " + name
        web.redirected = 1
        raise web.seeother('/apps')