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

        # raise this if our ending value is out of bounds
        if self.stop > 0xffffffffffff:
            raise ValueError, 'Last MAC address > ff:ff:ff:ff:ff:ff'

        # start zhe loop
        for i in range(self.start, self.stop):

            i = iter('%012x' % i)
            self.result.append( ':'.join([a+b for a,b in zip(i,i)]) )

    def __iter__(self):
        self.i = -1
        return self

    def next(self):

        self.i += 1
        try:
            return self.result[self.i]
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
