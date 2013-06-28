#### python tools to make my life easier


##### colors.py: python module for xterm colors

    >>> from colors import Color
    >>> Color.RED
    '\x1b[31m'
    >>> print Color.RED, 'RED', Color.END
    RED
    >>> Color.test()
    Foregound colors:
    BLACK COLOR
    RED COLOR
    GREEN COLOR
    YELLOW COLOR
    BLUE COLOR
    MAGENTA COLOR
    CYAN COLOR
    WHITE COLOR

    Background colors:
    BGBLACK COLOR
    BGRED COLOR
    BGGREEN COLOR
    BGYELLOW COLOR
    BGBLUE COLOR
    BGMAGENTA COLOR
    BGCYAN COLOR
    BGWHITE COLOR
    >>>

##### generator.py: python module for MAC and IP address generation

    >>> import generator
    >>> 
    >>> g = generator.GeneratorMAC('00:01:38:2a:00:00', 6)
    >>> 
    >>> for mac in g: mac
    ... 
    '00:01:38:2a:00:00'
    '00:01:38:2a:00:01'
    '00:01:38:2a:00:02'
    '00:01:38:2a:00:03'
    '00:01:38:2a:00:04'
    '00:01:38:2a:00:05'
    >>>
    >>> g = generator.GeneratorIP('172.16.13.22', 3)
    >>> 
    >>> for ip in g: ip
    ... 
    '172.16.13.22'
    '172.16.13.23'
    '172.16.13.24'


##### subnet.py: simple python module for ip network calculations


    >>> import subnet
    >>> s1 = subnet.Subnet('10.20.30.40', 30)
    >>> s2 = subnet.Subnet('10.20.30.40', '255.255.255.252')
    >>>
    >>> s1.get_network()
    '10.20.30.40'
    >>> s1.get_broadcast()
    '10.20.30.43'
    >>> s1.get_hosts()
    ['10.20.30.40', '10.20.30.41', '10.20.30.42', '10.20.30.43']
