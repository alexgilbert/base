from .abstract_model import AbstractModel
import datetime

class Session(AbstractModel):
    key = ''
    user = object()
    expires = datetime.datetime.now()
    
    