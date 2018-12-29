from conf.functions import *
from connection.app_connection import AppConnection
import hashlib

class AddApp:
    
    def GET(self):
        render = create_render(web.config._session.get('privilege'))
        return render.add_app()
    
    def POST(self):
        data = web.input()
        existingApp = AppConnection.find_by_name(name = data.name)
        existingUrl = AppConnection.find_by_url(url = data.url)
        render = create_render(web.config._session.get('privilege'))
        if hasattr(existingApp, 'name'):
            web.config._session.error = "App name already in use.\n"
            return render.add_app()
        elif hasattr(existingUrl, 'name'):
            web.config._session.error = "App Url already in use.\n"
            return render.add_app()
        else:
            AppConnection.add(data)
            web.config._session.message = "App " + data.name + "Successfully Created"
            web.config._session.redirected = 1
            raise web.seeother('/apps')
        
        
class Apps:
    
    def GET(self):
        render = create_render(web.config._session.get('privilege'))
        apps = AppConnection.get_apps()
        return render.apps(apps)
    

class EditApp:
    
    def GET(self, name):
        render = create_render(web.config._session.get('privilege'))
        existingApp = AppConnection.find_by_name(name)
        if hasattr(existingApp, 'name'):
            return render.edit_app(existingApp)
        else:
            web.config._session.error = "Unable to find " + name;
            web.config._session.redirected = 1
            raise web.seeother('/apps')
     
     
class UpdateApp:
    
    def POST(self):
        data = web.input()
        error = 0
        if data.existing != data.name:
            newAppFound = AppConnection.find_by_name(data.name)
            if hasattr(newAppFound, "name"):
                web.config._session.error = "New App Name already in use"
                error = 1
        newUrlFound = AppConnection.find_by_url(data.url)
        if hasattr(newUrlFound, "name") and newUrlFound.name != data.existing:
                web.config._session.error = "New App URL already in use"
                error = 1         
        web.config._session.redirected = 1
        if error == 0:
            success = AppConnection.update(data)
            if success == 1:
                web.config._session.message = "App successfully updated"
            else:
                web.config._session.error = "Error in updating app"
            raise web.seeother('/apps')
        else:
            raise web.seeother('/edit_app/'+data.existing)            

class DeleteApp:
    
    def GET(self, name):
        success = AppConnection.del_by_name(name)
        if success == 1:
            web.config._session.message = name + " Successfully Deleted"
        else:
            web.config._session.error = "Error: Unable to delete " + name
        web.config._session.redirected = 1
        raise web.seeother('/apps')
    

class DeactivateApp:
    
    def GET(self, name):
        success = AppConnection.deactivate_by_name(name)
        if success == 1:
            web.config._session.message = name + " Successfully Deactivated"
        else:
            web.config._session.error = "Error: Unable to deactivate " + name
        web.config._session.redirected = 1
        raise web.seeother('/apps')


class ActivateApp:
    
    def GET(self, name):
        success = AppConnection.activate_by_name(name)
        if success == 1:
            web.config._session.message = name + " Successfully Activated"
        else:
            web.config._session.error = "Error: Unable to activate " + name
        web.config._session.redirected = 1
        raise web.seeother('/apps')