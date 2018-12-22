import web

def my_loadhook():
    print("my load hook")
    web.config._session.error = ''
    web.config._session.message = ''


def my_unloadhook():
    print ("my unload hook")
    

def get_user_datafile():
    session = web.config._session
    if session.get('dev', False):
        return '/developer/base/data/user_dev'
    else:
        return '/developer/base/data/user'
    
    
def logged():
    session = web.config._session
    if session.get('login', False):
        return True
    else:
        return False

def create_render(privilege):
    if privilege == 0:
        render = web.template.render('templates/', base='reader', globals={'context': web.config._session})
    elif privilege == 1:
        render = web.template.render('templates/', base='user', globals={'context': web.config._session})
    elif privilege == 2:
        render = web.template.render('templates/', base='admin', globals={'context': web.config._session})
    else:
        render = web.template.render('templates/', base='reader', globals={'context': web.config._session})
    return render