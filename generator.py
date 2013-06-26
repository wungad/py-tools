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
        for i in range(self.start, self.stop + 1):

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
