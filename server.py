import socketserver

def handle_list(ip_addr, which_list):
    print('Add this to a list{}, {}'.format(ip_addr, which_list))

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        data_string = str(self.data)
        if 'list' in data_string:
            dt = data_string.split('::')
            ip_addr = dt[1]
            print(dt[0])
            which_list=True if 'whitelist' in dt[0] else False

            handle_list(ip_addr, which_list)

        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9000

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    try:
        server.serve_forever()
    except:
        server.server_close()
