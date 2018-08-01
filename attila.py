def get_properties(property):
    interfaces = ['Eth1', 'Eth2', 'Eth3']
    facts = {'hostname': 'ASR1', 'vendor': 'cisco'}

    if property == 'interfaces':
        return_value = interfaces
    elif property == 'facts':
        return_value = facts
    else:
        return_value = 'Invalid Property'
    print return_value

###xxx='interfaces'
###get_properties(xxx)
