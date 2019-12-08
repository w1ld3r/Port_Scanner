import sys
import argparse
import parser
import port_scanner.scanner as scanner


# define DEBUG state
DEBUG = False

def parse_arguments():
    """Define possible arguments"""
    desc = """Port scanner outputting its results as an HTML page."""
    # use argparse to parse args
    parser = argparse.ArgumentParser(prog='scanner', description=desc)
    parser.add_argument('-t', '--target',
        metavar='Target',
        help='Can pass hostnames, IP addresses, networks.\nEx: scanme.nmap.org; microsoft.com/24; 192.168.0.1; 192.168.0.0/24;', 
        nargs='+')
    parser.add_argument('-p', '--port',
        metavar='Port',
        help='Only scan specified ports.\nEx: -p 22; -p 80,443; -p 1-65535;',
        nargs='?')
    parser.add_argument('-o', '--ouput',
        metavar='Output path',
        help='Path of the output file.\nEx: /home/user',
        nargs='?')
    parser.add_argument('-f', '--file', 
        metavar='File',
        help='File containing a target list (host, ip, cidr)',
        type=argparse.FileType('r'),
        nargs='+')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(2)
    else:
        return get_args(parser.parse_args())

def file_tolist(args, hosts):
    """Words from file to list"""
    for file in args.file:
        for line in file:
            for word in line.split():
                hosts.add(word)
    return hosts
    
def get_args(args):
    """Arguments to list"""
    # List immutable for args
    hosts = set()
    port = ""
    path = ""
    try:
        if args.target:
            for target in args.target:
                hosts.add(target)
        if args.port:
            port = args.port
        if args.ouput:
            path = str(args.ouput)
        if args.file:
            hosts = file_tolist(args, hosts)
    except:
        sys.exit('Input not reconize !\n')
    if DEBUG:
        print(hosts)
    return hosts,port,path

def main():
    hosts,port,path = parse_arguments()
    if hosts:
        scanner.run(hosts, port, path)