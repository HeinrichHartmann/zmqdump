# zmqdump

### NAME
zmqdump - dump zmq messages on a socket

### SYNOPSIS

    zmqdump [options] [socket_type] endpoint


### DESCRIPTION

The zmqdump utility is used to make zmq socket communication available
on the unix shell. It can be used to listen to messages on SUB and
PULL sockets and to send messages out via PUB, PUSH sockets. 

The default behavior will dump all revceived messages on `stdout`; all
lines(!) received on `stdin` will be sent out as string messages.

Common uses include:  
- network testing  
- simple zmq proxies  
- shell script based zmq applications  

The options are as follows:

* The __socket_type__ can be one of the following options "PUB",
  "SUB", "PUSH", "PULL" (tbd: "PAIR", "REQ", "REP", "ROUTER",
  "DEALER"). If no __socket_type__ is provided, the "SUB" socket will
  be used.
  
* The __endpoint__ is a string consiting of two parts:
 
        endpoint = transport://address

  The __transport__ part specifies the underlying transport protocol
  and can be one of the following options: "inproc", "ipc", "tcp",
  "pgm", "epgm". The __address__ syntax is protocl dependent
  (cf. <http://api.zeromq.org/4-0:zmq-bind>)

* -d __delay__ spefifies an initial delay in milliseconds before
  sending out messages in order to address the
  [slow joiner syndrom](http://zguide.zeromq.org/page:all#Slow-Subscriber-Detection-Suicidal-Snail-Pattern).

* -s __pattern__ is only relevant for the "SUB" socket type. It allows
  to subscribe to specific patterns. The default is ("") -
  subscription to all messages.

* -b, --bind  
  bind to socket instead of connecting to it.

* -hwm __limit__ set a
  [high water mark](http://api.zeromq.org/3-2:zmq-setsockopt) on the
  socket. Default is 1000.

### EXAMPLES

Capture all messages on a PUB socket to a file:

    zmqdump SUB tcp://127.0.0.1:5000 > filename.out

Distribute lines of a file on a PUSH socket

    zmqdump --bind PUSH tpc://*:5000 < filename.in

Publish output of a script on socket:

    ./script | zmqdump --bind PUSH tpc://*:5000

Capitalize all messages in a pipeline

    zmqdump PULL $IN_EP | sed 's/[^ _-]*/\u&/g' | zmqdump PUSH $OUT_EP

