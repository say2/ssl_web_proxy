#!/usr/bin/python

import socketserver
import sys
import socket,ssl
import os

con_m='HTTP/1.1 200 Connection established\r\n'


class myhandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(4096).strip()
        print self.data
        if 'CONNECT' in self.data:
            self.request.sendall(con_m)
            d=self.data
            host = d[d.find('Host:') + 6:].split('\n')[0][:-1]
            self.make_site_key(host)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock=ssl.wrap_socket(s, keyfile=self.root_key, certfile=self.site_cert, server_side=True)
            self.sock.connect(host,443)



        #self.request.sendall(self.data.upper())

    def make_site_key(self,host):
        if not os.path.exists('./site_key/{}.pem'.format(host)):
            os.system('./site_key/make_site.sh {}'.format(host))
        self.root_key='./root/root.key'
        self.site_cert='./site_key/{}.crt'.format(host)

    def get_request(self):





if __name__=="__main__":
    bind_ip='localhost'
    bind_port=4433
    interface = "en0"

    server=socketserver.TCPServer((bind_ip,bind_port),myhandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(-1)


