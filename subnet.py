import socket
import struct

class Subnet(object):
    '''
    Easy subnet calc:
    '''
    def __init__(self, ip, mask=32):
        'You can provide decimal or dot notation'
        self.ip = None
        self.network = None
        self.broadcast = None
        self.netmask = None
        
        try:
            i = int(mask)
            self.netmask = (2 ** 32) - (2 ** (32 - mask))
        except ValueError:
            self.netmask = struct.unpack('!L', socket.inet_aton(mask))[0]
        finally:
            self.ip = struct.unpack('!L', socket.inet_aton(ip))[0]
            self.network = self.ip & self.netmask
            self.inv_netmask = (~ self.netmask) & 0xFFFFFFFF
            self.broadcast = self.inv_netmask | self.network
            
    def __repr__(self):
        return "class Subnet('%s', '%s')" % (self.get_network(), self.get_netmask())

    def __eq__(self,other):
        return self.network == other.network
        
    def get_ip(self):
        'Returns ip address'

        return socket.inet_ntoa(struct.pack('!L', self.ip))

    def get_netmask(self):
        'Returns network mask' 

        return socket.inet_ntoa(struct.pack('!L', self.netmask))

    def get_network(self):
        'Returns network address'

        return socket.inet_ntoa(struct.pack('!L', self.network))

    def get_broadcast(self):
        'Returns broadcast address'

        return socket.inet_ntoa(struct.pack('!L', self.broadcast))

    def get_hosts(self):
        '''
        Returns a list of all possible hosts.
        Broadcast and network address included.
        '''
        return [socket.inet_ntoa(struct.pack('!L', ip)) for ip in range(self.network, self.broadcast + 1)]

    def contains_ip(self, ip):
        'Returns True if ip is in network object'

        thisip  = struct.unpack("!L", socket.inet_aton(ip))[0]

        if (thisip >= self.network) and (thisip <= self.broadcast):
            return True
        else:
            return False

