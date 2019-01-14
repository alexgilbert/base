import web, sys
from routes import *

def my_loadhook():
    reset = 1
    if web.config._session.get('redirected') == 1:
        reset = 0
        web.config._session.redirected = 0
    if reset == 1:
        web.config._session.error = ''
        web.config._session.message = ''
    uri = get_request_uri()
    if uri in admin_urls:
        if web.config._session.get('privilege') != "2":
            web.config._session.error = "You do not have permissions to view this page"
            web.config._session.redirected = 1
            raise web.seeother('/')


def get_request_uri():
    uri_split = web.ctx.env['REQUEST_URI'].split('/')
    return "/" + uri_split[1]
    

def my_unloadhook():
    print ("my unload hook")
    

def logged():
    if web.config._session.get('login', False):
        return True
    else:
        return False


def create_render(privilege):
    privilege = str(privilege)
    if privilege == "0":
          render = web.template.render('/development/base/templates', base='reader', globals={'context': web.config._session})
    elif privilege == "1":
          render = web.template.render('/development/base/templates', base='user', globals={'context': web.config._session})
    elif privilege == "2":
          render = web.template.render('/development/base/templates', base='privileged', globals={'context': web.config._session})
    else:
          render = web.template.render('/development/base/templates', base='reader', globals={'context': web.config._session})
    return render
