import shelve
d = shelve.open("example") # open, with (g)dbm filename -- no suffix
d["hello"] = data   # store data at key (overwrites old data if
                # using an existing key)
data = d["hello"]   # retrieve a COPY of the data at key (raise
                # KeyError if no such key) -- NOTE that this
                # access returns a *copy* of the entry!
#del d[key]      # delete data stored at key (raises KeyError
                # if no such key)
flag = "hello" in d # true if the key exists
print(flag)
list = d.keys() # a list of all existing keys (slow!)
print (list)
d.close()       # close it
