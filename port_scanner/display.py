import sys
import port_scanner.helper as helper

def starting(version, time, nb, i):
    """Print nmap version and start time"""
    # message to print
    msg = 'Starting Nmap %s at %s' % (version, time)
    progress(i, nb, msg)

def ending(nb_ip, duration, nb, i):
    """Print number of IP scanned and duration"""
    # message to print
    msg = '%s IP address scanned in %s seconds' % (nb_ip, duration)
    i = nb # end
    progress(i, nb, msg)

def host_info(hostname, ip, nb, i):
    """Parse ip and hostanme and print these value"""
    # message to print
    msg = 'Scanning %s (%s)' % (hostname, ip)
    progress(i, nb, msg)

def no_port(nb, i):
    """Print no open ports found"""
    # message to print
    msg = '| No open ports found'
    progress(i, nb, msg)

def port(p_nb, p_type, p_state, p_service, nb, i):
    """Parse port number, service, version and print port number"""
    # message to print
    msg = '| Port %s/%s %s %s' % (p_nb, p_type, p_state, p_service)
    progress(i, nb, msg)

def cve(cve, nb, i):
    """Print no open ports found"""
    # message to print
    msg = '|\t%s' % (cve)
    progress(i, nb, msg)

def result(hosts):
    """Print summary"""
    # message to print
    msg = '%d IP addresses scanned, %d open ports and %d CVE found !\n' % (helper.count_host(hosts), helper.count_open_port(hosts), helper.count_cve(hosts))
    sys.stdout.write(msg)
    sys.stdout.flush()

def progress(count, total, suffix=''):
    """Display a progress bar"""
    # len of the bar
    bar_len = 20
    # len of filled bar
    filled_len = int(round(bar_len * count / float(total)))
    # calculate percentage
    percents = round(100.0 * count / float(total), 1)
    # create str filled bar 
    bar = '#' * filled_len + ' ' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s \t %s\n' % (bar, percents, '%', suffix))
    sys.stdout.flush()