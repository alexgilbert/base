import hashlib
from functions import *
from user_connection import UserConnection

class Admin:
    
    def GET(self):
        render = create_render()
        return render.admin()