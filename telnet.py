import json
facts = {'platform' : 'nexus' , 'model' : '9396' , 'hostname' : 'NX01' , 'vendor' : 'cisco'}

factsd = json.dumps(facts, indent=4)
print facts
print type(factsd)