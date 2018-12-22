from lib.shelf import shelf

class UserConnection:
    
    @staticmethod
    def add(user):
        user.locked = 0
        user.privilege = 1
        data = shelf.open('user')
        data[user.username] = user
        data.close()
    
    @staticmethod
    def find_by_username(username):
        try:
            data = shelf.open('user')
            user = data[username]
            data.close()
            return user
        except:
            return object()