from connection.user_connection import UserConnection
from model.user import User

userConnection = UserConnection()
user = User()
user.first = "Alex"
user.last = "Gilbert"
user.username = "agilbert7911"
user.password = "password"

userConnection.add(user)
foundUser = userConnection.findByUsername('agilbert7911')
print(foundUser.username)
print(foundUser.first)
print(foundUser.last)
