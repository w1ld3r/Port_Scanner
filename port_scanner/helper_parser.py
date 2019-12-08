import socket
import re


def merge_two_set(x, y):
    """Merge two set"""
    z = x.copy()
    z.update(y)
    return z

def merge_three_set(a, b, c):
    """Merge three set"""
    y = a.copy()
    y.update(b)
    z = merge_two_set(y, c)
    return z

def get_ipv6(input):
    """Get valide ipv6"""
    ipv6_hosts = set()
    for host in input:
        try:
            socket.inet_pton(socket.AF_INET6, host)
            ipv6_hosts.add(host)
        except socket.error:
            continue
    return ipv6_hosts

def get_ipv4(input):
    """Get valide ipv4"""
    ipv4_hosts = set()
    for host in input:
        try:
            socket.inet_pton(socket.AF_INET, host)
            ipv4_hosts.add(host)
        except socket.error:
            continue
    return ipv4_hosts

def get_hostname(input):
    """Get valide hostname"""
    hostname = set()
    for host in input:
        try:
            socket.gethostbyname(host)
            hostname.add(host)
        except socket.error:
            continue
    return hostname

def get_ipv4_cidr(input):
    """Get valide ipv4 cidr"""
    s_cidr = set()
    for host_cidr in input:
        if re.match(r"^.*[^\/][\/]{1}\d+$", host_cidr):
            host,cidr = host_cidr.split("/")
            t_host = [host]
            if (get_ipv4(t_host) or get_hostname(t_host)) and re.match(r"^([1-9]|1[0-9]|2[0-9]|3[0-2])$", cidr):
                    s_cidr.add(host_cidr)
        else:
            continue
    return s_cidr

def get_ipv6_cidr(input):
    """Get valide ipv6 cidr"""
    s_cidr = set()
    for host_cidr in input:
        if re.match(r"^.*[^\/][\/]{1}\d+$", host_cidr):
            host,cidr = host_cidr.split("/")
            t_host = [host]
            if get_ipv6(t_host) and re.match(r"^(12[0-8]|1[01][0-9]|[1-9]?[0-9])$", cidr):
                    s_cidr.add(host_cidr)
        else:
            continue
    return s_cidr

def get_port(input):
    """Get valide port"""
    if input:
        # if match between 1 and 65535 (ex: 1337)
        if re.match(r"^([1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$", input):
            return input
        # if match between 1 and 65535 with comma separator (ex: 1,2,3)
        elif re.match(r"^([1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])(,([1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5]))+$", input):
            return input
        # if match between 1 and 65535 of port range (ex: 80-443)
        elif re.match(r"^([1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])-([1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$", input):
            return input
    return None

def get_hosts_up(d_hosts):
    """Get hostame of hosts with ports open/closed/filtered"""
    hosts = []
    for key in d_hosts:
        if d_hosts[key].ports:
            hosts.append(d_hosts[key].hostname)
    return hosts

def get_ports_open(d_hosts):
    """Get port number of host up"""
    ports = set()
    for key in d_hosts:
        if d_hosts[key].ports:
            for nb in d_hosts[key].ports:
                if d_hosts[key].ports[nb].state == "open":
                    ports.add(d_hosts[key].ports[nb].number)
    return ports