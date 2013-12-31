import unittest

# use symlink in test directory
# ln -s ../zmqdump zmqdump.py
from zmqdump import *

class TestArgParse(unittest.TestCase):

    parser = None

    def setUp(self):
        self.parser = setup_parser()

    def tearDown(self):
        pass

    def testArgs(self):
        def pArgStr(s): 
            return self.parser.parse_args(s.split())

        ns = pArgStr("SUB tcp://127.0.0.1:8000")
        self.assertEqual(ns.socket_type, "SUB")
        self.assertEqual(ns.endpoint, "tcp://127.0.0.1:8000")
        self.assertEqual(ns.hwm, 1000)
        self.assertEqual(ns.bind, False)
        self.assertEqual(ns.delay, 0)
        
        ns = pArgStr("PUB tcp://127.0.0.1:8000 -d 200 -b")
        self.assertEqual(ns.socket_type, "PUB")
        self.assertEqual(ns.endpoint, "tcp://127.0.0.1:8000")
        self.assertEqual(ns.hwm, 1000)
        self.assertEqual(ns.bind, True)
        self.assertEqual(ns.delay, 200)
        
        ns = pArgStr("PULL tcp://127.0.0.1:8000")
        self.assertEqual(ns.socket_type, "PULL")
        self.assertEqual(ns.endpoint, "tcp://127.0.0.1:8000")
        self.assertEqual(ns.hwm, 1000)
        self.assertEqual(ns.bind, False)
        self.assertEqual(ns.delay, 0)

        ns = pArgStr("PULL tcp://127.0.0.1:8000 -hwm 1")
        self.assertEqual(ns.socket_type, "PULL")
        self.assertEqual(ns.endpoint, "tcp://127.0.0.1:8000")
        self.assertEqual(ns.hwm, 1)
        self.assertEqual(ns.bind, False)
        self.assertEqual(ns.delay, 0)

        ns = pArgStr("--bind PUSH -hwm 1 tcp://127.0.0.1:8000 -d 100 ")
        self.assertEqual(ns.socket_type, "PUSH")
        self.assertEqual(ns.endpoint, "tcp://127.0.0.1:8000")
        self.assertEqual(ns.hwm, 1)
        self.assertEqual(ns.bind, True)
        self.assertEqual(ns.delay,  100)

if __name__ == '__main__':
    unittest.main()
