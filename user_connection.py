import shelf

class UserConnection:
    
    @staticmethod
    def add(user):
        user.locked = "0"
        user.privilege = "1"
        del user.confirm
        data = shelf.open('/development/base/data/user_data')
        data[user.username] = user
        data.close()
    
    @staticmethod
    def update(user):
        try:
            data = shelf.open('/development/base/data/user_data')
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
            data = shelf.open('/development/base/data/user_data')
            user = data[username]
            data.close()
            return user
        except Exception as e:
            print(e)
            return object()
    
    @staticmethod
    def del_by_username(username):
        try:
            data = shelf.open('/development/base/data/user_data')
            del data[username]
            data.close()
            return 1
        except Exception as e:
            print(e)
            return 0
        
    @staticmethod
    def set_lock_by_username(username, lock):
        try:
            data = shelf.open('/development/base/data/user_data')
            user = data[username]
            user.locked = str(lock)
            data[username] = user
            data.close()
            return 1
        except Exception as e:
            print(e)
            return 0
        
    @staticmethod
    def lock_by_username(username):
        return UserConnection.set_lock_by_username(username, 1)
    
    @staticmethod
    def unlock_by_username(username):
        return UserConnection.set_lock_by_username(username, 0)
    
    @staticmethod
    def get_users():
        try:
            data = shelf.open('/development/base/data/user_data', flag="r")
            users = []
            for key in data:
                users.append(data[key])
            data.close()
            print(users)
            return users
        except Exception as e:
            print(e)
            return {}