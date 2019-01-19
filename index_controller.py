import web, os
from functions import *
from user_app_connection import UserAppConnection
from app_connection import AppConnection

class index:
    def GET(self):
        print("there")
        render = create_render()
        apps = []
        if logged():
            user_apps = UserAppConnection.find_apps_by_username(web.ctx.session.username)
            for user_app in user_apps:
                app = AppConnection.find_by_name(user_app)
                if hasattr(app, 'name'):
                    apps.append(app)
            return render.index(apps)
        else:
            print("not logged inn")
            web.seeother('/signin')
            
    def POST(self):
        print("here")
        render = create_render()
        apps = []
        if logged():
            user_apps = UserAppConnection.find_apps_by_username(web.ctx.session.username)
            for user_app in user_apps:
                app = AppConnection.find_by_name(user_app)
                if hasattr(app, 'name'):
                    apps.append(app)
            return render.index(apps)
        else:
            print("not logged in")
            web.seeother('/signin')
        
class static:
    def GET(self, media, file):
        try:
            f = open('/development/base/' + media + '/'+file, 'r')
            return f.read()
        except Exception as e:
            print(e)
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

        if name in os.listdir('/development/base/images'):  # Security
            web.header("Content-Type", cType[ext]) # Set the Header
            return open('/development/base/images/%s'%name,"rb").read() # Notice 'rb' for reading images
        else:
            raise web.notfound()
    