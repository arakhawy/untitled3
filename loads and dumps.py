import json
"""from json import loads
from json import dumps"""
facts = '{"hostname": "nxosv", "os": "7.3", "location": "San_Jose" , "ahmed" : 33}'
print(facts)
print type(facts)

factsd = json.loads(facts)
print (factsd)
print type(factsd)

factsf = json.dumps(factsd)
print (factsf)
print type(factsf)



