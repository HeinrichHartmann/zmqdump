#!/usr/bin/env python
#
# zmqdump - dump zmq messages on a socket
#
# https://github.com/HeinrichHartmann/zmqdump
#
# @author: Heinrich Hartmann <derhein@gmail.com>
#
# License: GPLv2

import argparse
import sys

def main():
    parser = setupParser()
    conf = parser.parse_args()
    socket = openSocket(conf)
    printLoop(socket)

def setupParser():
    parser = argparse.ArgumentParser(
        prog = "zmqdump",
        description = "dump zmq messages on a socket"
    )

    parser.add_argument(
        "socket_type", 
        help= "type of zmq socket.", 
        type = str,
        choices = ["SUB","PUB","PUSH","PULL","REQ","REP"]
    )

    parser.add_argument(
        "endpoint", 
        help="endpoint to listen on messages (tcp://127.0.0.1)",
        type = str
    )

    parser.add_argument(
        "-d", "--delay", 
        help = "initial delay before sendig out messages",
        dest = "delay", type = int, default = 0
    )
    parser.add_argument(
        "-hwm", 
        help="High water mark.",
        dest="hwm", type=int, default = 1000
    )

    parser.add_argument(
        "-b", "--bind",
        help="bind socket instead of connect",
        dest="bind", default = False,
        action = "store_true"
    )

    return parser

## TESTS ##
def test():
    testSetupParser()

def testSetupParser():

    parser = setupParser()

    parser.print_help()

    def pArgStr(s):
        print "> " + s
        ns =  parser.parse_args(s.split())
        print ns
        return ns

    ns = pArgStr("SUB tcp://127.0.0.1:8000")
    assert (ns.socket_type == "SUB")
    assert (ns.endpoint == "tcp://127.0.0.1:8000")
    assert (ns.hwm == 1000)
    assert (ns.bind == False)
    assert (ns.delay == 0)

    ns = pArgStr("PUB tcp://127.0.0.1:8000 -d 200 -b")
    assert (ns.socket_type == "PUB")
    assert (ns.endpoint == "tcp://127.0.0.1:8000")
    assert (ns.hwm == 1000)
    assert (ns.bind == True)
    assert (ns.delay == 200)

    ns = pArgStr("PULL tcp://127.0.0.1:8000")
    assert (ns.socket_type == "PULL")
    assert (ns.endpoint == "tcp://127.0.0.1:8000")
    assert (ns.hwm == 1000)
    assert (ns.bind == False)
    assert (ns.delay == 0)

    ns = pArgStr("PULL tcp://127.0.0.1:8000 -hwm 1")
    assert (ns.socket_type == "PULL")
    assert (ns.endpoint == "tcp://127.0.0.1:8000")
    assert (ns.hwm == 1)
    assert (ns.bind == False)
    assert (ns.delay == 0)

    ns = pArgStr("--bind PUSH -hwm 1 tcp://127.0.0.1:8000 -d 100 ")
    assert (ns.socket_type == "PUSH")
    assert (ns.endpoint == "tcp://127.0.0.1:8000")
    assert (ns.hwm == 1)
    assert (ns.bind == True)
    assert (ns.delay == 100)
    
if __name__ == "__main__":
    test()
    main()


