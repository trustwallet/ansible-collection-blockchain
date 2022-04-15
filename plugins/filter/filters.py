def to_cosmos_peers(peers):
    result = []
    for peer in peers:
       result.append("%s@%s" % (peer['id'], peer['address'])) 
    
    return ','.join(result)

class FilterModule(object):

    def filters(self):
        return {
            'to_cosmos_peers': to_cosmos_peers,
        }
