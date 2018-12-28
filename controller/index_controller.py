import web
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
   def GET(self,fileName):
       imageBinary = open("./images/"+fileName,'rb').read()
       return imageBinary