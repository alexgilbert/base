import sys
sys.path.insert(0, '/development/base/lib/shelf')
import shelf

class ShelfConnection( object ):
    
    def open_connection(self, model):
        if hasattr(model, 'file'):
            return shelf.open(model.file)
        
    def close_connection(self, data):
        data.close()