import re
import port_scanner.nmap_parser as nmap_parser
from port_scanner.host import Host
from port_scanner.port import Port


def create_host(result, p_hosts):
    """Contruct the result dictionnary"""
    current_host = 0
    current_port = 0
    hosts = p_hosts
    for line in result:
        if re.match(r"^Nmap scan report for.*$", line):
            # get current host
            current_host = nmap_parser.get_hostname(line)
            # if host not in dic
            if current_host not in hosts:
                # create host
                hosts[current_host] = Host(nmap_parser.get_hostname(line), nmap_parser.get_ip(line))
        elif re.match(r"^\d+/\w+\s+\w+\s+.*$", line):
            # get current port
            current_port = nmap_parser.get_port_number(line)
            # if port not in dic
            if current_port not in hosts[current_host].ports:
                # create host
                hosts[current_host].ports[current_port] = Port(current_port, nmap_parser.get_port_type(line), nmap_parser.get_port_state(line), nmap_parser.get_service_port(line))
            # if port service version found
            if len(line.split()) > 3:
                # set port service version
                hosts[current_host].ports[current_port].set_service_version(nmap_parser.get_service_version(line))
        # if mac address found
        elif re.match(r"^MAC Address.*$", line):
            # set mac address on current host
            hosts[current_host].set_mac_address(nmap_parser.get_mac(line))
        # if os version found
        elif re.match(r"^Running.*$", line):
            # set os version to current host
            hosts[current_host].set_os_version(nmap_parser.get_os_version(line))
        # if cve found
        elif re.match(r"^[\|].*CVE.*$", line):
            # add cve to current port in current host
            hosts[current_host].ports[current_port].set_cve(nmap_parser.get_cve(line))
        # if anonymous login found
        elif re.match(r"^.*account has empty password$", line) or re.match(r"^.*State: VULNERABLE$", line) or re.match(r"^.*Anonymous FTP login allowed.*$", line):
            # set anonymous login at true to current port in current host
            hosts[current_host].ports[current_port].set_anonymous_login()
        # if screenshot taken
        elif re.match(r"^[\|].*Saved to.*$", line):
            # set screenshot filename to current port in current host
            hosts[current_host].ports[current_port].set_screenshot(nmap_parser.get_screenshot(line))
    # return dic of Host
    return hosts

        
            