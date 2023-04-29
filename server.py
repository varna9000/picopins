import http.server
import socketserver
import os
import time

class CustomHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    bus = {'i2c','uart','spi','pwm'}
    params = {'all','pins','find'}

    def do_GET(self):
        p = self.path.split('/')
        arguments=[]
        buses=[]

        for parameter in p:
            if parameter in self.params:
                arguments.append(f"--{parameter}")

            if (parameter[:4] == 'find') and ("all" in p):
                    f_what = parameter.split('-')[1]
                    arguments.append(f'--find "{f_what}"')

            if parameter in self.bus:
                buses.append(parameter)

        cmd = f'unbuffer {os.path.dirname(os.path.realpath(__file__))}/env/bin/python picopins/__main__.py {" ".join(buses)} {" ".join(arguments)} > index.txt'
        print(cmd)
        os.system(cmd)

        self.path = "index.txt"
        time.sleep(1)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8002

handler = CustomHttpRequestHandler
server=socketserver.TCPServer(("", PORT), handler)
print(f"Server started at port {PORT}. Press CTRL+C to close the server.")
try:
	server.serve_forever()
except KeyboardInterrupt:
	server.server_close()
	print("Server Closed")
