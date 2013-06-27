class GeneratorMAC(object):
    '''
    MAC address generator
    '''
    def __init__(self, start='0', count=1):
        
        # sanitize and normalize
        start = start.replace(':', '').replace('-', '').replace('.', '')
        start = int(start, 16)

        self.start = start
        self.stop = start + count
        self.result = []
        self.i = -1

        # raise this if our ending value is out of bounds
        if self.stop > 0xffffffffffff:
            raise ValueError, 'Last MAC address > ff:ff:ff:ff:ff:ff'

        # start zhe loop
        for i in range(self.start, self.stop):

            self.result.append(i)


    def _nice(self, integer):
        
        _iter = iter('%012x' % integer)
        return ':'.join([a+b for a,b in zip(_iter, _iter)])

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.result)
        
    def __getitem__(self, key):

        # index
        if isinstance(key, int):

            try: return self._nice(self.result[key])
            except IndexError:
                raise IndexError, "Index out of range"
        # slice
        elif isinstance(key, slice):

            (start, stop, step) = key.indices( len(self) )
            data = self.result[start:stop:step]
            
            return [self._nice(mac) for mac in data]

        # other
        else:
            raise TypeError, "Integer expected"

    def next(self):

        self.i += 1
        try:
            return self._nice(self.result[self.i])
        except IndexError:
            raise StopIteration

class GeneratorIP(object):
    '''
    IP address generator
    '''
    def __init__(self, start='192.168.0.0', count=255):
        import socket
        import struct

        start = struct.unpack('!L', socket.inet_aton(start))[0]
        stop = start + count

        self.result = []
        for i in range(start, stop):

            ip = socket.inet_ntoa(struct.pack('!L', i))
            self.result.append(ip)
        

    def __iter__(self):

        self.i = -1
        return self


    def next(self):

        self.i += 1
        try:
            return self.result[self.i]
        except IndexError:
            raise StopIteration
