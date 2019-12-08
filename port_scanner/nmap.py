import shlex
import subprocess
import os.path
import port_scanner.nmap_parser as nmap_parser


IPV6_BASIC = ' -6 -T4 -sS -O -v '
IPV4_BASIC = ' -T4 -sS -O -v '
IPV4_SCREENSHOT = ' -n -sS -v -sC --script=http-screenshot '
IPV6_SCREENSHOT = ' -6 -n -sS -v -sC --script=http-screenshot '

def run(options, targets , ports=None):
        if (options == IPV4_SCREENSHOT or options == IPV6_SCREENSHOT) and not os.path.isfile("/usr/share/nmap/scripts/http-screenshot.nse"):
            return ''
        elif ports:
                if options == IPV4_BASIC or options == IPV6_BASIC:
                    cmd = 'nmap' + options + '-p ' + ' '.join(targets) + ' -p ' + ports
                else:
                    cmd = 'nmap' + options + '-p ' + ','.join(ports) + ' ' + ' '.join(targets)
        else:
            cmd = "nmap" + options + ' '.join(targets)
        # make cmd readable by subprocess.Popen
        cmd = shlex.split(cmd)
        # create a nmap process 
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return nmap_parser.parse(process, targets)