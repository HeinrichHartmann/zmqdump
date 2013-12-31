import unittest
import zmq
import time

# use symlink in test directory
from zmqdump import *

class TestArgParse(unittest.TestCase):

    pub_socket   = None
    pub_endpoint = "ipc://tmp/zmqdump/test_pub"

    def setUp(self):
        c = zmq.Context()
        self.pub_socket = c.socket(zmq.PUB)
        self.pub_socket.bind(pub_endpoint)
        

    def testSendMessages(self):
        conf = parseArgs("SUB " + pub_endpoint)
        self.sock = setupSocket(conf)

        time.sleep(0.1)
        
        msg = "Hello World"
        pub_socket.send(msg)
        self.assertEqual(sock.recv(), msg)
        

    def tearDown(self):
        self.pub_socket.close()

if __name__ == '__main__':
    unittest.main()
