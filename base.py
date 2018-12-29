import web, sys
sys.path.insert(0, '')
from conf.functions import *
from conf.routes import *


web.config.debug = True

app = web.application(urls, globals())

store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'login': 0, 'privilege': "0", 'username': 'Guest', 'redirected': 0})
web.config._session = session

from controller.index_controller import *
from controller.user_controller import *
from controller.login_controller import *
from controller.admin_controller import *
from controller.app_controller import *
from controller.user_app_controller import *

render = web.template.render('templates/', globals={'context': session})

app.add_processor(web.loadhook(my_loadhook))
app.add_processor(web.unloadhook(my_unloadhook))

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()