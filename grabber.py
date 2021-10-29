from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys

hostName = "localhost"
serverPort = 8050

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
       self.send_response(302)
       self.send_header('Location', sys.argv[1])
       self.end_headers()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Grabber started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
