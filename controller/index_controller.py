import web, os
from conf.functions import *
from connection.user_app_connection import UserAppConnection
from connection.app_connection import AppConnection

class index:
    def GET(self):
        render = create_render(web.config._session.get('privilege'))
        apps = []
        if logged():
            user_apps = UserAppConnection.find_apps_by_username(web.config._session.get('username'))
            for user_app in user_apps:
                app = AppConnection.find_by_name(user_app)
                apps.append(app)
        return render.index(apps)
    

class static:
    def GET(self, media, file):
        try:
            f = open(media+'/'+file, 'r')
            return f.read()
        except:
            return ''
        

class ImageDisplay(object):
    
    def GET(self,name):
        ext = name.split(".")[-1] # Gather extension
        cType = {
            "png":"images/png",
            "jpg":"images/jpeg",
            "gif":"images/gif",
            "ico":"images/x-icon"
            }

        if name in os.listdir('images'):  # Security
            web.header("Content-Type", cType[ext]) # Set the Header
            return open('images/%s'%name,"rb").read() # Notice 'rb' for reading images
        else:
            raise web.notfound()
    