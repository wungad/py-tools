#!/usr/bin/env python
import re
import getopt
import sys
import os
import subprocess

 
# CONFIGURATION - change as needed
tcpdump_bin = "/usr/local/sbin/tcpdump"
tcpdump_opts = [ 
    '-s0',
    '-v',
]

tcpdump_expr = [
]

# structures
isc_types = {
    'DISCOVER': 1,
    'OFFER':    2,
    'REQUEST':  3,
    'DECLINE':  4,
    'ACK':      5,
    'NAK':      6,
    'RELEASE':  7,
    'IFNORM':   8
}

# helper funcs
def usage():

    print 'Usage:', os.path.basename(__file__), '-h | -i INTERFACE [-t TYPE] [-n NETWORK/BITS ] [-g GATEWAY] [-m MAC]'
    print '\t-h or --help: prints this help'
    print '\t-i or --interface: network interface to listen on (default: eth0)'
    print
    print '\t-t or --type: dhcp packet to match (default: all packets are dumped)'
    print '\t\tTYPE can be any of the following:'
    for k in isc_types.keys():
        print '\t\t%s' % k
    print
    print '\t-n or --network: network address/bits to match(default: 0.0.0.0/0)'
    print '\t-g or --gateway: gateway ip address to match (default: all gateways)'
    print '\t\tNOTE: gateway ip address is not available in lease extension packets'
    print
    print '\t-m or --mac: mac address to match (default: all addresses)'
    sys.exit(0)

def fatal(msg):

    print 'FATAL:', msg.strip()
    sys.exit(1)

# init options
try: options = getopt.getopt(sys.argv[1:], 'hi:c:t:n:g:m:', ['help', 'interface=', 'count=', 'type=', 'network=', 'gateway=', 'mac='])[0]
except getopt.GetoptError: usage()

if not options: usage()

arg_interface = 'eth0'
arg_count     = None
arg_type      = None
arg_gateway   = None
arg_mac       = None
arg_network   = '0.0.0.0/0'

# parse options
for (opt, val) in options: 

    if opt in ['-h', '--help']: usage()
    elif opt in ['-i', '--interface']: arg_interface = val
    elif opt in ['-c', '--count']: arg_count = val
    elif opt in ['-t', '--type']: arg_type = val
    elif opt in ['-n', '--network']: arg_network = val
    elif opt in ['-g', '--gateway']: arg_gateway = val
    elif opt in ['-m', '--mac']: arg_mac = val
    else: usage()


# construct command
tcpdump_opts.append("-i %s" % arg_interface)

if arg_count != None:

    try: int(arg_count)
    except: fatal('Need integer type, got %s instead' % arg_count)
    else: tcpdump_opts.append("-c %s" % arg_count)

if arg_type != None:

    try: tcpdump_expr.append("udp[250:1] == 0x%d" % isc_types[arg_type])
    except: fatal('unknown message type: %s' % arg_type)

if arg_type != None:

    tcpdump_expr.append("src net %s" % arg_network)

if arg_gateway != None:

    try: gw = re.match(r'(^\d+\.\d+\.\d+\.\d+$)', arg_gateway).group(1)
    except: fatal("Need IP type x.x.x.x got %s instead" % arg_gateway)
    else: 
        gw = ''.join(['%02x' % int(x) for x in gw.split('.')])
        tcpdump_expr.append('udp[32:4] == 0x%s' % gw)

if arg_mac != None:

    try: mac = re.match(r'(^([0-9a-f]{2}:){5}[0-9a-f]{2}$)', arg_mac, re.IGNORECASE).group(1)
    except: fatal("Need MAC type xx:xx:xx:xx:xx:xx, got %s instead" % arg_mac)
    else: 
        mac1 = ''.join(mac.split(':')[:4])
        mac2 = ''.join(mac.split(':')[4:])
        tcpdump_expr.append('udp[36:4] == 0x%s' % mac1)
        tcpdump_expr.append('udp[40:2] == 0x%s' % mac2)

tcpdump_command = "%s %s '%s'" % (tcpdump_bin, ' '.join(tcpdump_opts), ' && '.join(tcpdump_expr))

print
print 'Starting TCPDUMP with command:', tcpdump_command
print
os.system(tcpdump_command)
