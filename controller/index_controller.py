import web, os
from conf.functions import *

class index:
    def GET(self):
        print("login: " + str(web.config._session.get('login')))
        print("priv: " + str(web.config._session.get('privilege')))
        print("username: " + str(web.config._session.get('username')))
        render = create_render(web.config._session.get('privilege'))
        return render.index()
    

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
    