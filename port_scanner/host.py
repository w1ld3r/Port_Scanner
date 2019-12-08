class Host:
    """Host object representing a host"""
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip
        self.ports = {}
        self.mac = None
        self.os = None

    def set_mac_address(self, mac_address):
        """Host @mac setter"""
        # set @mac in aray of all hosts
        self.mac = mac_address

    def set_os_version(self, os_version):
        """Host os version setter"""
        # set os version in aray of all hosts
        self.os = os_version
        return self



