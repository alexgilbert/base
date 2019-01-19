import web, sys
from variables import *

def my_loadhook():
    reset = 1
    if web.ctx.session.redirected == 1:
        reset = 0
        web.ctx.session.redirected = 0
    if reset == 1:
        web.ctx.session.error = ''
        web.ctx.session.message = ''
    uri = get_request_uri()
    if uri in admin_urls:
        if web.ctx.session.privilege != "2":
            web.ctx.session.error = "You do not have permissions to view this page"
            web.ctx.session.redirected = 1
            raise web.seeother('/')


def get_request_uri():
    uri_split = web.ctx.env['REQUEST_URI'].split('/')
    return "/" + uri_split[1]
    

def my_unloadhook():
    print ("my unload hook")
    

def logged():
    print("login = " + str(web.ctx.session.login))
    if web.ctx.session.login == 1:
        return True
    else:
        return False


def create_render():
    privilege = web.ctx.session.privilege
    if privilege == "0":
          render = web.template.render('/development/base/templates', base='reader', globals={'context': web.ctx.session})
    elif privilege == "1":
          render = web.template.render('/development/base/templates', base='user', globals={'context': web.ctx.session})
    elif privilege == "2":
          render = web.template.render('/development/base/templates', base='privileged', globals={'context': web.ctx.session})
    else:
          render = web.template.render('/development/base/templates', base='reader', globals={'context': web.ctx.session})
    return render
