import sys
import os


def numberofip(targets):
    """Calculate number of host to scan"""
    i = 0
    for e in targets:
        # if cidr
        if "/" in e:
            (_, cidr) = e.split("/")
            cidr = int(cidr)
            if(cidr <= 32):
                i += 2**(32-cidr)
            else:
                i += 2**(128-cidr)
        else:
            i += 1
    return i

def count_host(results):
    """Count number of ip scanned"""
    i = 0
    for _ in results:
        i += 1   
    return i

def count_open_port(results):
    """Count number of open ports scanned"""
    i = 0
    for key in results:
        if results[key].ports:
            for nb in results[key].ports:
                if results[key].ports[nb].state == "open":       
                    i += 1
    return i

def count_cve(results):
    """Count number of cve scanned"""
    i = 0
    for key in results:
        if results[key].ports:
            for nb in results[key].ports:
                if results[key].ports[nb].cve:
                    for _ in results[key].ports[nb].cve:  
                        i += 1
    return i

def print_report_path(filename):
    """Print the path and filename of the scan report"""
    sys.stdout.write("\nNmap scan report saved as: %s" % filename)

def print_screenshot_path(results):
    """Print the path and filename of the screenshot"""
    for key in results:
        if results[key].ports:
            for nb in results[key].ports:
                if results[key].ports[nb].screenshot:
                    sys.stdout.write("\nScreenshot saved in current working directory as: %s" % results[key].ports[nb].screenshot)

    