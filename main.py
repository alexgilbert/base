from connection.user_connection import UserConnection
import hashlib

userConnection = UserConnection()
user = {"first":"Alex", "last":"Gilbert", "locked":0,
        "username":"agilbert7911", "privilege":3,
        "password":hashlib.sha256(("sAlT754-"+"Bluoct12").encode('utf-8')).hexdigest()}
print(user)

#userConnection.add(user)
#foundUser = userConnection.findByUsername('agilbert7911')
#print(foundUser.username)
#print(foundUser.first)
#print(foundUser.last)
#print(foundUser.password)
#print(foundUser.privilege)
#print(foundUser.locked)