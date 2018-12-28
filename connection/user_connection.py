from lib.shelf import shelf

class UserConnection:
    
    @staticmethod
    def add(user):
        user.locked = 0
        user.privilege = 1
        del user.confirm
        data = shelf.open('data/user_data')
        data[user.username] = user
        data.close()
    
    @staticmethod
    def update(user):
        try:
            data = shelf.open('data/user_data')
            del data[user.existing]
            del user['existing']
            data[user.username] = user
            data.close
            return 1
        except Exception as e:
            print(e)
            return 0
        
    @staticmethod
    def find_by_username(username):
        try:
            data = shelf.open('data/user_data', flag="r")
            print(data['agilbert7911'])
            user = data[username]
            data.close()
            return user
        except:
            return object()
    
    @staticmethod
    def del_by_username(username):
        try:
            data = shelf.open('data/user_data')
            del data[username]
            return 1
        except Exception as e:
            print(e)
            return 0
        
    @staticmethod
    def get_users():
        try:
            data = shelf.open('data/user_data', flag="r")
            users = []
            for key in data:
                users.append(data[key])
            data.close()
            print(users)
            return users
        except Exception as e:
            print(e)
            return {}