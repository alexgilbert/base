import sys
sys.path.insert(0, '/development/base/lib/shelf')
import shelf
import datetime

class SessionConnection(object):
    file = 'data/session'
    
    def add(self, session):
        now = datetime.datetime.now()
        now_plus_30 = now + datetime.timedelta(minutes = 30)
        session.expires = now_plus_30 
        
        data = shelf.open(self.file)
        data[session.key] = session
        data.close()
        
    def findByKey(self, key):
        data = shelf.open(self.file)
        session = data[key]
        data.close()
        return session