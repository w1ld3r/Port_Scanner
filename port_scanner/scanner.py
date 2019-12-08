import port_scanner.nmap as nmap
import port_scanner.generate as generate
import port_scanner.helper_parser as helper_parser
import port_scanner.display as display
import port_scanner.multi_process as multi_process 


IPV6_BASIC = ' -6 -T4 -sS -O -v '
IPV4_BASIC = ' -T4 -sS -O -v '
IPV4_CVE = ' -sV -sS -v --script vulners '
IPV6_CVE = ' -6 -sV -sS -v --script vulners '
IPV4_SCREENSHOT = ' -n -sS -v -sC --script=http-screenshot '
IPV6_SCREENSHOT = ' -6 -n -sS -v -sC --script=http-screenshot '
IPV4_HTTP_LOGIN = ' -sS --script=http-frontpage-login '
IPV6_HTTP_LOGIN = ' -6 -sS --script=http-frontpage-login '
IPV4_EMPTY_PASSWORD = ' -sV -sS --script=mysql-empty-password '
IPV6_EMPTY_PASSWORD = ' -6 -sV -sS --script=mysql-empty-password '
IPV4_FTP_ANON = ' -sV -sC -sS '
IPV6_FTP_ANON = ' -sV -sC -sS '

def first_round(hosts, ports):
    """Function to realize a first nmap dicovery"""
    # structure to stock results from nmap
    results = {}
    # structure to stock tasks of nmap
    tasks = []

    # set of hosts by type
    ipv4_hosts = helper_parser.get_ipv4(hosts)
    ipv6_hosts = helper_parser.get_ipv6(hosts)
    hostname = helper_parser.get_hostname(hosts)
    ipv4_cidr = helper_parser.get_ipv4_cidr(hosts)
    ipv6_cidr = helper_parser.get_ipv6_cidr(hosts)
    # get valide ports
    ports = helper_parser.get_port(ports)

    if ipv6_cidr or ipv6_hosts:
        # put ipv6 and ipv6 cidr in a set
        s_hostsipv6 = helper_parser.merge_two_set(ipv6_hosts,ipv6_cidr)
        # convert dictionnary to list
        l_hostsipv6 = list(s_hostsipv6)
        # append task
        tasks.append((nmap.run, (IPV6_BASIC, l_hostsipv6, ports)))

    if ipv4_hosts or hostname or ipv4_cidr:
        # put ipv4, hostname and ipv4 cidr in a set
        s_hostsipv4 = helper_parser.merge_three_set(ipv4_hosts,hostname, ipv4_cidr)
        # convert dictionnary to list
        l_hostsipv4 = list(s_hostsipv4)
        # create task
        tasks.append((nmap.run, (IPV4_BASIC, l_hostsipv4, ports)))
    
    # make a first basic scan for discovery open port
    results = multi_process.run(results, tasks)

    return second_round(results)

def second_round(results):
    """Function to make a deep nmap scan"""
    # list of host for deep scann
    hosts_up = helper_parser.get_hosts_up(results)
    # list of port for deep scann
    ports_open = helper_parser.get_ports_open(results)

    if hosts_up and ports_open:
        # structure to stock tasks of nmap
        tasks = []
        # set of hosts by type
        ipv4_hosts = helper_parser.get_ipv4(hosts_up)
        ipv6_hosts = helper_parser.get_ipv6(hosts_up)
        hostname = helper_parser.get_hostname(hosts_up)
        ipv4_cidr = helper_parser.get_ipv4_cidr(hosts_up)
        ipv6_cidr = helper_parser.get_ipv6_cidr(hosts_up)

        if ipv6_cidr or ipv6_hosts:
            # put ipv6 and ipv6 cidr in a set
            s_hostsipv6 = helper_parser.merge_two_set(ipv6_hosts,ipv6_cidr)
            # convert dictionnary to list
            l_hostsipv6 = list(s_hostsipv6)
            # append tasks
            tasks.append((nmap.run, (IPV6_CVE, l_hostsipv6, ports_open)))
            tasks.append((nmap.run, (IPV6_SCREENSHOT, l_hostsipv6, ports_open)))
            tasks.append((nmap.run, (IPV6_HTTP_LOGIN, l_hostsipv6, ports_open)))
            tasks.append((nmap.run, (IPV6_EMPTY_PASSWORD, l_hostsipv6, ports_open)))
            tasks.append((nmap.run, (IPV6_FTP_ANON, l_hostsipv6, ports_open)))
            
        if ipv4_hosts or hostname or ipv4_cidr:
            # put ipv4, hostname and ipv4 cidr in a set
            s_hostsipv4 = helper_parser.merge_three_set(ipv4_hosts,hostname, ipv4_cidr)
            # convert set to list
            l_hostsipv4 = list(s_hostsipv4)
            # append tasks
            tasks.append((nmap.run, (IPV4_CVE, l_hostsipv4, ports_open)))
            tasks.append((nmap.run, (IPV4_SCREENSHOT, l_hostsipv4, ports_open)))
            tasks.append((nmap.run, (IPV4_HTTP_LOGIN, l_hostsipv4, ports_open)))
            tasks.append((nmap.run, (IPV4_EMPTY_PASSWORD, l_hostsipv4, ports_open)))
            tasks.append((nmap.run, (IPV4_FTP_ANON, l_hostsipv4, ports_open)))
        
        # make a deeper scan
        results = multi_process.run(results, tasks)

    # display a short summary
    display.result(results)
    return results

def run(hosts, ports, path):
    """Main function of the scanner"""
    multi_process.freeze_support()
    if hosts:
        results = first_round(hosts, ports)
        if results:
            generate.html(results, path)
