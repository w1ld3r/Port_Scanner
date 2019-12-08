import os
import sys
import port_scanner.main as main
import port_scanner.scanner as scanner


# check sudo and env
if os.getuid() != 0:
    sys.exit('Must be run as root')

hosts,ports,path = main.parse_arguments()
if hosts:
    scanner.run(hosts, ports, path)