class Port:
    """Port object representing a port"""
    def __init__(self, number, type, state, service):
        self.number = number
        self.type = type
        self.state = state
        self.service = service
        self.version = None
        self.cve = []
        self.screenshot = None
        self.anonymous_login = False
        
    def set_service_version(self, version):
        """Port service version setter"""
        self.version = version

    def set_cve(self, cve):
        """Port cve setter"""
        self.cve.append(cve)

    def set_screenshot(self, screenshot):
        """Port scrteenshot setter"""
        self.screenshot = screenshot

    def set_anonymous_login(self):
        """Port anonymous login setter"""
        self.anonymous_login = True