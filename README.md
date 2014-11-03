ping-pong
==============

ping-pong is a simplistic set of python scripts used to test what TCP ports are available on a server.  This was quickly thrown together to allow developers determine if their application's network connectivity is being blocked by network firewalls.  The environment did not permit the use of network sniffers so this is a basic alternative.

To execute the test place pong.py on the server and ping.py on the client.

On the server, execute the code by executing:
```
$ python pong.py
```

On the client, execute the code by executing:
```
$ python ping.py <server_ip>
```

Todo:

* add UDP tests
* add better reports
