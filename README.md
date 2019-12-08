# Port Scanner

Port scanner using nmap, outputting its results as an HTML page.

With port_scanner, multiple nmap are executed in parallel using python multiprocessing.

Compatible with IPv4 and IPv6 addresses.


## Getting Started

### Prerequisites

Install python3 and pip:
```
sudo apt install python3 python3-pip
```

Install Nmap:
```
sudo apt install nmap
```

Install the necessary Python packages:
```
sudo pip3 install -r requirements.txt
```

To perform screenshot of website:
```
sudo apt install wkhtmltopdf
sudo wget -O /usr/share/nmap/scripts/http-screenshot.nse \ https://raw.githubusercontent.com/leostat/Necurity.co.uk/master/scripts/http-screenshot.nse
sudo nmap --script-updatedb
```

### Installing

The installation has been tested in Debian bullseye/sid x86_64 (december 2019)

#### Clone the project
```
git clone https://github.com/x1n5h3n/port_scanner.git
```

#### Move in the project folder
```
cd port_scanner
```

#### Install using pip
```
sudo pip3 install .
```

### Usage

Should be run with root privileges.

To scan an ip address on a particular port:
```
sudo run-scanner -t 192.168.1.1 -p 22
```

To scan an ip address on a multiple ports:
```
sudo run-scanner -t 192.168.1.1 -p 22,80,443
```

To scan an ip address on a port range:
```
sudo run-scanner -t 192.168.1.1 -p 1-65535
```

To scan an hostname:
```
sudo run-scanner -t nmap.org
```

To scan a cidr:
```
sudo run-scanner -t 192.168.1.0/24 nmap.org/24
```

Use a targets file:
```
sudo run-scanner -f targets.txt
```

Specify the output path of the html scan report:
```
sudo run-scanner -t 192.168.1.1 -o /home/user
```

Print help:
```
sudo run-scanner -h
```

## Authors

* **[x1n5h3n](https://github.com/x1n5h3n)**

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.

