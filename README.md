#### python tools to make my life easier

#### pls.py: simple quick and dirty playlist parser
    >>> import pls
    >>> p = pls.Playlist('mp4.pls')
    >>> p.getVersion()
    '2'
    >>> p.getFileByTitle('EUROSPORT')
    'udp://@232.4.2.25:5002'

##### ripeq: tool for querying RIPE database
    $ ./ripeq 2a00:ee0::/32
    inet6num         2a00:ee0::/29
    netname          SI-TELEKOM-20081120
    descr            Telekom Slovenije d.d.
    remarks          ISP in Slovenia
    country          SI
    ...

##### isc_dump.py: Linux/Solaris tool for dumping ISC DHCP traffic with handy filters
	EXAMPLE: dumping DISCOVER packets on bnx27000 coming from relay ip 10.160.56.1:
	$ sudo isc_dump.py -i bnx27000 -t DISCOVER -g 10.159.12.1
	Starting TCPDUMP with command: /usr/local/sbin/tcpdump -s0 -v -i bnx27000 'udp[250:1] == 0x1 && udp[32:4] == 0x0a9f0c01'

	tcpdump: listening on bnx27000, link-type EN10MB (Ethernet), capture size 65535 bytes
	09:23:57.251181 IP (tos 0x0, ttl 253, id 55122, offset 0, flags [none], proto UDP (17), length 385)
		10.159.12.1.bootps > tr69-dhcp.bootps: BOOTP/DHCP, Request from 00:01:38:9f:00:61 (oui Unknown), length 357, hops 1, xid 0xda070000, secs 8704, Flags [Broadcast]
          Gateway-IP 10.159.12.1
          Client-Ethernet-Address 00:01:38:00:00:00 (oui Unknown)
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message Option 53, length 1: Discover
            Lease-Time Option 51, length 4: 86000
            Requested-IP Option 50, length 4: 10.159.15.242
            Vendor-Class Option 60, length 28: "IskraTEL Ganymede822+ Router"
            Parameter-Request Option 55, length 8:
              Subnet-Mask, BR, Time-Zone, Default-Gateway
              Classless-Static-Route, Domain-Name, Domain-Name-Server, Hostname
            Agent-Information Option 82, length 55:
              Circuit-ID SubOption 1, length 53: ISKRATEL:DS03_6666-RE_ipBAN_unknown_101 atm 1/12:1.33

##### nef_cleaner.py: windows tool for deleting .nef files which have not .jpg pair
    my wife asked for this :D
##### isis.py: python module for ISIS dump parsing
    >>> from isis import Database, Record
    >>> db = Database('ISIS-DATABASE.txt')
    >>> db.get_hostnames()
    >>> db.get_addresses()
    >>> db.get_records()

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
