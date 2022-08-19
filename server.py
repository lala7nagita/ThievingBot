from http.server import BaseHTTPRequestHandler,HTTPServer
import json
import time 

path = "C:/Users/Kevin/Desktop/PyBot/live_data.json"
# http://127.0.0.1:80/

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        #print("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()
      
        data = json.loads(self.data_string)
        with open(path, "w") as outfile:
            try:
                json.dump(data, outfile, indent=4)
            except json.decoder.JSONDecodeError:
                return
        return

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    #print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))

else:
    run()

