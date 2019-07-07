"""Sockets"""
import socket
import argparse

PARSER = argparse.ArgumentParser(description='Test Sockets')
PARSER.add_argument('--url',
                    dest='url',
                    action='store',
                    default='localhost',
                    help='address for server')
PARSER.add_argument('--port',
                    dest='port',
                    action='store',
                    default=80,
                    help='port for work')
ARGS = PARSER.parse_args()
URL = ARGS.url
PORT = ARGS.port


def run(url, port):
    """Run sockets"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (url, port)
    s.connect(addr)
    s.send(b'GET / HTTP/1.0\r\n\r\n')
    resp = s.recv(1024)
    s.close()
    return resp


request = run(URL, PORT)
print(request)


if __name__ == '__main__':
    run(URL, PORT)
