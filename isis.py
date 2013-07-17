'''
Parser for ISIS database dump
from ERICSSON SmartEdge Router
'''
class Record(object):
    '''
    Single entry
    '''
    def __init__(self, block):

        self.block = block
        self.hostname = None
        self.address = None
        self.routes = []
        self.__parse_block()

    def __parse_block(self):

        for line in self.block:

            if line.startswith('  Hostname: '): self.hostname = line.split()[1]
            elif line.startswith('  IP Address: '): self.address = line.split()[2]
            elif '  Metric: ' in line  and 'IP ' in line: self.routes.append(line.split()[3])

class Database(object):
    '''
    Database file
    '''
    def __init__(self, filename):

        self.filename = filename
        self.lines = open(filename).readlines()
        self.records = []
        self.__parse_lines()


    def get_records(self):
        'Returns list if Record() objects'

        return self.records

    def get_hostnames(self):
        'Returns found hostnames'

        return [r.hostname for r in self.records]

    def get_addresses(self):
        'Returns found ip addresses'

        return [r.address for r in self.records]

    def __parse_lines(self):

        block = []

        block.append(self.lines.pop(0))
        in_block = True

        for line in self.lines:

            if not line.startswith('  '):

                self.records.append(Record(block))
                block = []
                block.append(line)
            else:
                block.append(line)

        self.records.append(Record(block))

#db = Database('ISIS-DATABASE.txt')

#for r in db.get_records():

#    print r.hostname
#    print r.address
#    print r.routes
