import json
rakhawy = { 'a' : 1 , 'b' : 2 , 'c' : 3}
print rakhawy
print type(rakhawy)
ahmedr = rakhawy.json.dumps()

print ahmedr
print type(ahmedr)


ahmeds = json.loads(ahmedr)

print ahmeds
print type(ahmeds)