from conf.functions import *
from connection.user_connection import UserConnection
import hashlib

class Admin:
    
    def GET(self):
        render = create_render(web.config._session.get('privilege'))
        return render.admin()