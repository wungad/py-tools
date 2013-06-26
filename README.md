#### python tools to make my life easier

##### subnet.py

simple python module for ip network calculations


#### example usage:

    $ python
    Python 2.6.6 (r266:84292, Feb 22 2013, 00:00:18)
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import subnet
    >>> s1 = subnet.Subnet('10.20.30.40', 29)
    >>> s2 = subnet.Subnet('10.20.30.40', '255.255.255.0')
    >>>
    >>> s1.get_network()
    '10.20.30.40'
    >>>
    >>> s2.get_network()
    '10.20.30.0'
    >>>
    >>> s1.get_broadcast()
    '10.20.30.47'
    >>>
    >>> s2.get_broadcast()
    '10.20.30.255'
    >>>
    >>> s1.get_hosts()
    ['10.20.30.40', '10.20.30.41', '10.20.30.42', '10.20.30.43', '10.20.30.44', '10.20.30.45', '10.20.30.46', '10.20.30.47']
    >>>
    
    
