from lib.shelf import shelf

class UserAppConnection:
    
    @staticmethod
    def add_app_to_user(username, app):
        try:
            data = shelf.open('data/user_app_data')
            if username in data:
                userApps = data[username]
                userApps.add(app)
            else:
                userApps = set()
                userApps.add(app)
            data[username] = userApps
            data.close()
            return 1
        except Exception as e:
            print(e)
            return 0
        
    @staticmethod
    def find_apps_by_username(username):
        try:
            data = shelf.open('data/user_app_data', flag="r")
            apps = data[username]
            data.close()
            return apps
        except:
            return set()
        
    @staticmethod
    def remove_app_from_user(username, app):
        try:
            data = shelf.open('data/user_app_data')
            if username in data:
                apps = data[username]
                apps.remove(app)
                data[username] = apps
            data.close()
            return 1
        except Exception as e:
            print(e)
            return 0