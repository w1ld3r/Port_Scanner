import sys
import os
try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    sys.exit("Please install Jinja2")
from datetime import datetime
import port_scanner.helper as helper


def html(results, path):
    """Create an html file with results"""
    # current directory
    root = os.path.dirname(os.path.abspath(__file__))
    # templates dir
    templates_dir = os.path.join(root, 'templates')
    # Create the jinja2 environment.
    env = Environment(loader=FileSystemLoader(templates_dir), trim_blocks=True)
    # get template
    template = env.get_template('index.html')
        
    # get now time
    now = datetime.now().strftime("%H:%M:%S %d/%m/%Y")

    if not os.path.isdir(path):
        # set default path to current working directory
        path = os.getcwd()
    # define nmap scan report filename
    filename = "index.html"
    # define output filename and path
    filename = os.path.join(root, path, filename)    
    
    with open(filename, 'w') as fh:
        # write to output file using jinja2
        fh.write(template.render(
                date=now,
                hosts=results,
                nb_ip=helper.count_host(results),
                nb_open_port=helper.count_open_port(results),
                nb_cve=helper.count_cve(results),
                path=os.getcwd(),
        ))
    
    # print the path of the nmap scan report file
    helper.print_report_path(filename)
    