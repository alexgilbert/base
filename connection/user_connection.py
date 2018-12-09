import sys
sys.path.insert(0, '/development/base/lib/shelf')
import shelf

class UserConnection(object):
    file = 'data/user'
    
    def add(self, user):
        user.locked = 0
        user.privilege = 1
        data = shelf.open(self.file)
        data[user.username] = user
        data.close()
        
    def findByUsername(self, username):
        data = shelf.open(self.file)
        user = data[username]
        data.close()
        return user