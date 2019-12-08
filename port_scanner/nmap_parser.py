import re
import port_scanner.display as display
import port_scanner.helper as helper


# define DEBUG state
DEBUG = False

def parse(process, targets):
    """Display process and construct array of all scanned host"""
    # set number of scan host
    nb = helper.numberofip(targets) + 1
    # set progression counter
    i = 0
    # dictionary of host
    result = []

    # while process running
    while process.poll() is None:
        #add output line to line
        line = process.stdout.readline().decode('UTF-8')
        if re.match(r"^Starting Nmap.*$", line):
           display.starting(get_nmap_version(line), get_start_time(line), nb, i)
        elif re.match(r"^Nmap scan report for.*$", line):
            i += 1 # new scann - for progress bar
            # print host info
            display.host_info(get_hostname(line), get_ip(line), nb, i)
            # add line to result
            result.append(line)
        elif re.match(r"^All.*closed$", line):
            display.no_port(nb, i)
        elif re.match(r"^\d+/\w+\s+\w+\s+.*$", line):
            # print port info
            display.port(get_port_number(line), get_port_type(line), get_port_state(line), get_service_port(line), nb, i)
            # add line to result
            result.append(line)
        elif re.match(r"^MAC Address.*$", line):
            # add line to result
            result.append(line)
        elif re.match(r"^Running.*$", line):
            # add line to result
            result.append(line)
        elif re.match(r"^[\|].*CVE.*$", line):
            display.cve(get_cve(line), nb, i)
            # add line to result
            result.append(line)
        elif re.match(r"^[\|].*Saved to.*$", line):
            result.append(line)
        elif re.match(r"account has empty password$", line) or re.match(r"State: VULNERABLE$", line) or re.match(r"^.*Anonymous FTP login allowed.*$", line):
            result.append(line)
        elif re.match(r"^Nmap done.*seconds$", line):
            display.ending(get_nb_ip(line), get_duration(line), nb, i)
        if DEBUG:
            print(line)

    return result

def get_nmap_version(line):
    """Nmap version getter"""
    return ''.join(line.split()[2])

def get_start_time(line):
    """Nmap start time getter"""
    return ' '.join(line.split()[7:])

def get_ip(line):
    """Ip address getter"""
    return ''.join(re.findall(r'\(([^()]+)\)', line))

def get_hostname(line):
    """Hostname getter"""
    return ''.join(line.split()[4])

def get_port_number(line):
    """Port number getter"""
    return ''.join(line.split('/')[0])

def get_port_type(line):
    """Port type getter"""
    return ''.join(line.split('/')[1].split(' ')[0])

def get_port_state(line):
    """Port state getter"""
    return ''.join(line.split()[1])

def get_service_port(line):
    """Service port getter"""
    return ''.join(line.split()[2])

def get_service_version(line):
    """Service version getter"""
    return ' '.join(line.split()[3:])

def get_duration(line):
    """nmap duration getter"""
    return  ''.join(line.split()[10])

def get_nb_ip(line):
    """number of ip scanned getter"""
    return  ''.join(line.split()[2])

def get_mac(line):
    """address mac getter"""
    return line.split()[2]

def get_os_version(line):
    """os version getter"""
    return line.split(': ')[1].replace('\n', '')

def get_cve(line):
    """cve getter"""
    return ''.join(line.split()[1])

def get_screenshot(line):
    """screenshot name getter"""
    return ''.join(line.split()[3])