import socket
import sys

def send_message(ip_addr, bl):
    HOST, PORT = "localhost", 9000
    which_list = 'blacklist' if not bl else 'whitelist'

    data = '{}::{}'.format(which_list, ip_addr)

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
    finally:
        sock.close()

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
