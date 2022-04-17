from collections import OrderedDict                                 # Allows the use of ordered dictionaries

router1 = OrderedDict([('brand', 'Cisco'),
                        ('model', '1941'),
                        ('mgmtIP', '10.0.0.1'),                     # Creats an ordered dictionary variable
                        ('G0/0', '10.0.1.1'),                       # called "router1".
                        ('G0/1', '10.0.2.1'),
                        ('G0/2', '10.1.0.1')
                       ])
                        
for key in router1:                                                 # a 'for' loop that for each "key" in the ordered dictionary "router1"
    print("Key = " + key + "\t" + "Value = " + router1[key])        # we will print to the screen the desired text, each ordered
                                                                    # dictionary key and each ordered dictionary "value"
print()     # blank line printed for readability

interface = OrderedDict([('name', 'GigabitEthernet1'),
                         ('description', 'to port6.sandbox-backend'),
                         ('type',OrderedDict([
                             ('@xmlns:ianaift', 'urn:ietf:params:xml:ns:yang:iana-if-type'),
                             ('#text', 'ianaift:ethernetCsmacd')
                             ])
                          ),
                         ('enabled', 'true'),                                                   # Creates a nested ordered dictionary
                         ('ipv4', OrderedDict([                                                 # defined by the variable "interface".
                             ('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip'),
                             ('address', OrderedDict([
                                 ('ip', '10.10.20.175'),
                                 ('netmask', '255.255.255.0')
                                 ])
                              )]
                                              )
                          ),
                         ('ipv6', OrderedDict([
                             ('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip')]
                                              )
                          )
                         ])

name = interface['name']                                                                        # Here we are creating four different
text = interface['type']['#text']                                                               # variables, each corresponds with a
ipv4 = interface['ipv4']['address']['ip']                                                       # specific 'value' that is part of the
netmask = interface['ipv4']['address']['netmask']                                               # nested ordered dictionary "interface".

print("interface" + "\t  " + "text" + "\t\t\t  " + "IP address" + "\t" + "netmask")
print("-"*16 + "  " + "-"*22 + "  " + "-"*12 + "\t" + "-"*13)                                   # These series of print() statements
print(name + "  " + text + "  " + ipv4 + "\t" + netmask)                                        # print out the desired information, which
                                                                                                # is represented by the four variables we
                                                                                                # defined above, in a presentable human
                                                                                                # readable format










