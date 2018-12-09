import web
from connection.user_connection import UserConnection
from model.user import User
import hashlib

web.config.debug = False

render = web.template.render('templates/', base='layout')
urls = (
    '/', 'index',
    '/addUser', 'addUser',
    '/login', 'Login',
    '/(js|css|images|fonts)/(.*)', 'static', 
    '/reset', 'Reset'
    )

app = web.application(urls, globals())

store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'login': 0, 'privilege': 0})


class index:
    def GET(self):
        if logged():
            self.render = create_render(session.get('privilege'))
            return self.render.index()
        else:
            self.render = create_render(0)
            return self.render.index()

class addUser:
    userConnection = UserConnection()

    def GET(self):
        render = create_render(0)
        return render.registration()
    
    def POST(self):
        i = web.input()
        existingUser = self.userConnection.findByUsername(i.username)
        if i.password != i.confirm:
            self.render.password_missmatch()
        elif existingUser.username == i.username:
            self.render.user_exists(i.username)
        else:
            i.password = hashlib.sha1("sAlT754-"+i.password).hexdigest()
            self.userConnection.add(i)
            raise web.seeother('/')
            

def logged():
    if session.get('login', False):
        return True
    else:
        return False

def create_render(privilege):
    if logged():
        if privilege == 0:
            render = web.template.render('templates/reader')
        elif privilege == 1:
            render = web.template.render('templates/user')
        elif privilege == 2:
            render = web.template.render('templates/admin')
        else:
            render = web.template.render('templates/communs')
    else:
                ## This line is key, i do not have a communs folder, thus returning an unusable object
        #render = web.template.render('templates/communs')  #Original code from example

        render = web.template.render('templates/', base='layout')
    return render



class Login:
    userConnection = UserConnection()
    
    def GET(self):
        if logged():
            web.redirect('/')
        else:
            render = create_render(0)
            return render.login()

    def POST(self):
        name, passwd = web.input().username, web.input().password
        foundUser = self.userConnection.findByUsername(name)
        try:
            if hashlib.sha1("sAlT754-"+passwd).hexdigest() == foundUser.password:
                session.login = 1
                session.privilege = foundUser.privilege
                self.render = create_render(session.get('privilege'))
                return self.render.index()
            else:
                session.login = 0
                session.privilege = 0
                session.username = name
                self.render = create_render(session.get('privilege'))
                return self.render.login_error()
        except:
            session.login = 0
            session.privilege = 0
            self.render = create_render(session.get('privilege'))
            return self.render.login_error()


class Reset:

    def GET(self):
        session.login = 0
        session.kill()
        self.render = create_render(session.get('privilege'))
        return self.render.logout()

class static:
    def GET(self, media, file):
        try:
            f = open(media+'/'+file, 'r')
            return f.read()
        except:
            return ''
        
if __name__ == "__main__": app.run()