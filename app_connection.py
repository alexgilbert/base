import shelf

class AppConnection:
    
    @staticmethod
    def add(app):
        app.active = "1"
        data = shelf.open('/development/base/data/app_data')
        data[app.name] = app
        data.close()
        
    @staticmethod
    def update(app):
        try:
            data = shelf.open('/development/base/data/app_data')
            del data[app.existing]
            del app['existing']
            data[app.name] = app
            data.close
            return 1
        except Exception as e:
            print(e)
            return 0
        
    @staticmethod
    def find_by_name(name):
        try:
            data = shelf.open('/development/base/data/app_data', flag="r")
            app = data[name]
            data.close()
            return app
        except:
            return object()
        
    @staticmethod
    def find_by_url(url):
        try:
            data = shelf.open('/development/base/data/app_data', flag="r")
            for key in data:
                app = data[key]
                if app['url'] == url:
                    return app
            return object()
        except:
            return object()
    
    @staticmethod
    def del_by_name(name):
        try:
            data = shelf.open('/development/base/data/app_data')
            del data[name]
            data.close()
            return 1
        except Exception as e:
            print(e)
            return 0
        
    @staticmethod
    def set_active_by_name(name, active):
        try:
            data = shelf.open('/development/base/data/app_data')
            app = data[name]
            app.active = str(active)
            data[name] = app
            data.close()
            return 1
        except Exception as e:
            print(e)
            return 0
        
    @staticmethod
    def deactivate_by_name(name):
        return AppConnection.set_active_by_name(name, 0)
    
    @staticmethod
    def activate_by_name(name):
        return AppConnection.set_active_by_name(name, 1)
    
    @staticmethod
    def get_apps():
        try:
            data = shelf.open('/development/base/data/app_data', flag="r")
            apps = []
            for key in data:
                apps.append(data[key])
            data.close()
            return apps
        except Exception as e:
            print(e)
            return {}