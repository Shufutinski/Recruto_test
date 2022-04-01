from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        name = query_components.get("name")
        message = query_components.get("message")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Recruto</title></head>", "utf-16"))
        self.wfile.write(bytes(f"{name}! <br> {message}!" , "utf-16"))
        self.wfile.write(bytes("</html>", "utf-16"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")