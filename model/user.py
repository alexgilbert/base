from .abstract_model import AbstractModel

class User(AbstractModel):
    username = ''
    first = ''
    last = ''
    password = ''
    locked = 0