from port_scanner import helper_parser
import unittest


class Test_Parser(unittest.TestCase):
    """Parser test cases"""

    def test_ipv6(self):
        test = ['2a01:cb04:19:ec00:8f19:70a6:bb11:3842', '1200:0000:AB00:1234:0000:2552:7777:1313']
        value = helper_parser.get_ipv6(test)
        self.assertEqual(set(['2a01:cb04:19:ec00:8f19:70a6:bb11:3842','1200:0000:AB00:1234:0000:2552:7777:1313']), value)
    
    def test_bad_ipv6(self):
        test = ['foo','1200::AB00:1234::2552:7777:1313','1200:0000:AB00:1234:O000:2552:7777:1313']
        value = helper_parser.get_ipv6(test)
        self.assertEqual(set(), value)
    
    def test_ipv4(self):
        test = ['1.2.3.4','255.255.255.255']
        value = helper_parser.get_ipv4(test)
        self.assertEqual(set(['1.2.3.4','255.255.255.255']), value)
    
    def test_bad_ipv4(self):
        test = ['foo','1337.1337.1337.1337','1.2.3.4.5']
        value = helper_parser.get_ipv4(test)
        self.assertEqual(set(), value)

    def test_hostname(self):
        test = ['foo.com','foo.foo.com']
        value = helper_parser.get_hostname(test)
        self.assertEqual(set(['foo.com','foo.foo.com']), value)
    
    def test_bad_hostname(self):
        test = ['foo foo','foo!']
        value = helper_parser.get_hostname(test)
        self.assertEqual(set(), value)

    def test_ipv4_cidr(self):
        test = ['1.2.3.4/24','foo.com/32','foo.foo.com/1']
        value = helper_parser.get_ipv4_cidr(test)
        self.assertEqual(set(['1.2.3.4/24','foo.com/32','foo.foo.com/1']), value)
    
    def test_bad_ipv4_cidr(self):
        test = ['1.2.3.4//24','1.2.3.4/33','foo!/1']
        value = helper_parser.get_ipv4_cidr(test)
        self.assertEqual(set(), value)

    def test_ipv6_cidr(self):
        test = ['2a01:cb04:19:ec00:8f19:70a6:bb11:3842/128','21DA:D3:0:2F3B:2AA:FF:FE28:9C5A/1']
        value = helper_parser.get_ipv6_cidr(test)
        self.assertEqual(set(['2a01:cb04:19:ec00:8f19:70a6:bb11:3842/128','21DA:D3:0:2F3B:2AA:FF:FE28:9C5A/1']), value)
    
    def test_bad_ipv6_cidr(self):
        test = ['1200::AB00:1234::2552:7777:1313//1','21DA:D3:0:2F3B:2AA:FF:FE28:9C5A/129']
        value = helper_parser.get_ipv6_cidr(test)
        self.assertEqual(set(), value)
    
    def test_port1(self):
        test = '65535'
        value = helper_parser.get_port(test)
        self.assertEqual('65535', value)
    
    def test_port2(self):
        test = '1-65535'
        value = helper_parser.get_port(test)
        self.assertEqual('1-65535', value)
    
    def test_port3(self):
        test = '1,65535'
        value = helper_parser.get_port(test)
        self.assertEqual('1,65535', value)
    
    def test_bad_port1(self):
        test = 0
        value = helper_parser.get_port(test)
        self.assertEqual(None, value)
    
    def test_bad_port2(self):
        test = '65536'
        value = helper_parser.get_port(test)
        self.assertEqual(None, value)
    
    def test_bad_port3(self):
        test = '1-6553-'
        value = helper_parser.get_port(test)
        self.assertEqual(None, value)
    
    def test_bad_port4(self):
        test = '1,65535,'
        value = helper_parser.get_port(test)
        self.assertEqual(None, value)

if __name__ == '__main__':
    unittest.main()