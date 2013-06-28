class Color(object):
    '''
    Colors for my xterm
    '''

    MAP = {
        'BLACK':    30,
        'RED':      31,
        'GREEN':    32,
        'YELLOW':   33,
        'BLUE':     34,
        'MAGENTA':  35,
        'CYAN':     36,
        'WHITE':    37,
    
        'BGBLACK':  40,
        'BGRED':    41,
        'BGGREEN':  42,
        'BGYELLOW': 43,
        'BGBLUE':   44,
        'BGMAGENTA':45,
        'BGCYAN':   46,
        'BGWHITE':  47,
    }

    END     = '\033[0m'
    NUM     = '\033[%dm'
    
    BLACK   = NUM % MAP['BLACK']
    RED     = NUM % MAP['RED']
    GREEN   = NUM % MAP['GREEN']
    YELLOW  = NUM % MAP['YELLOW']
    BLUE    = NUM % MAP['BLUE']
    MAGENTA = NUM % MAP['MAGENTA']
    CYAN    = NUM % MAP['CYAN']
    WHITE   = NUM % MAP['WHITE']

    BGBLACK   = NUM % MAP['BGBLACK']
    BGRED     = NUM % MAP['BGRED']
    BGGREEN   = NUM % MAP['BGGREEN']
    BGYELLOW  = NUM % MAP['BGYELLOW']
    BGBLUE    = NUM % MAP['BGBLUE']
    BGMAGENTA = NUM % MAP['BGMAGENTA']
    BGCYAN    = NUM % MAP['BGCYAN']
    BGWHITE   = NUM % MAP['BGWHITE']

    @staticmethod
    def test():
        'Run this'
        print 'Foregound colors:'
        for name, val in sorted(Color.MAP.items(), key=lambda x: x[1])[:8]:

            print '%s%s COLOR %s' % (Color.NUM % val, name, Color.END)

        print

        print 'Background colors:'
        for name, val in sorted(Color.MAP.items(), key=lambda x: x[1])[8:]:

            print '%s%s COLOR %s' % (Color.NUM % val, name, Color.END)

            

__name__ == '__main__' and Color.test()
