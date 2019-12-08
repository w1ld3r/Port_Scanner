from port_scanner import main
import unittest
import sys


class Test_Args(unittest.TestCase):
    """Argparse test cases"""

    @unittest.expectedFailure
    def test_empty(self):
        with self.assertRaises(SystemExit):
            main.parse_arguments()

    def test_unrecognized_argument(self):
        sys.argv[1:]=['-x']
        with self.assertRaises(SystemExit):
            main.parse_arguments()

    def test_empty_target(self):
        sys.argv[1:]=['-t']
        with self.assertRaises(SystemExit):
            main.parse_arguments()
    
    def test_empty_file(self):
        sys.argv[1:]=['-f']
        with self.assertRaises(SystemExit):
            main.parse_arguments()
    
    def test_not_found_file(self):
        sys.argv[1:]=['-f', 'foo']
        with self.assertRaises(SystemExit):
            main.parse_arguments()

    def test_correct_target1(self):
        sys.argv[1:]=['-t','localhost']
        hosts,port,path = main.parse_arguments()
        self.assertEqual(set(['localhost']), hosts)
    
    def test_correct_target2(self):
        sys.argv[1:]=['-t','localhost', '0.0.0.0']
        hosts,port,path = main.parse_arguments()
        self.assertEqual(set(['localhost', '0.0.0.0']), hosts)

    def test_correct_target3(self):
        sys.argv[1:]=['-t','localhost/24']
        hosts,port,path = main.parse_arguments()
        self.assertEqual(set(['localhost/24']), hosts)
    
    def test_correct_target4(self):
        sys.argv[1:]=['-t','google.com']
        hosts,port,path = main.parse_arguments()
        self.assertEqual(set(['google.com']), hosts)

    def test_correct_target5(self):
        sys.argv[1:]=['-t','google.com/24']
        hosts,port,path = main.parse_arguments()
        self.assertEqual(set(['google.com/24']), hosts)

    def test_correct_target6(self):
        sys.argv[1:]=['-t','fe80::9eeb:e8ff:fe79:d5d4']
        hosts,port,path = main.parse_arguments()
        self.assertEqual(set(['fe80::9eeb:e8ff:fe79:d5d4']), hosts)

    def test_correct_port1(self):
        sys.argv[1:]=['-p','80']
        hosts,port,path = main.parse_arguments()
        self.assertEqual('80', port)
    
    def test_correct_port2(self):
        sys.argv[1:]=['-p','22,80,443']
        hosts,port,path = main.parse_arguments()
        self.assertEqual('22,80,443', port)
    
    def test_correct_port3(self):
        sys.argv[1:]=['-p','22-80-443']
        hosts,port,path = main.parse_arguments()
        self.assertEqual('22-80-443', port)

if __name__ == '__main__':
    unittest.main()