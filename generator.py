class GeneratorMAC(object):

    def __init__(self, count=1):
        
        self.count = count
        self.mac_list = []

        for i in range(count):

            i = iter('%012x' % i)
            self.mac_list.append( ':'.join([a+b for a,b in zip(i,i)]) )

    def generate(
    def __next__(self):
        pass
