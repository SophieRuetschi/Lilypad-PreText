#ChatGPT generated server- needed for custom handler to pass .wasm file
# TO DO: clean up 

import http.server
import socketserver
import mimetypes

# Define a custom handler to ensure .wasm files are served with the correct MIME type
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        # Use the default guess_type function first
        mime_type, encoding = mimetypes.guess_type(path)

        # If the file is a .wasm file, set the correct MIME type
        if path == '/external/lilypad-web/f69741145824184a2d8c.wasm':
            mime_type = 'application/wasm'
            print("converting type")
        
        return mime_type

# Define the port for the server
PORT = 8000

# Create a TCP server and run it with the custom handler
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving PreTeXt files at http://localhost:{PORT}")
    httpd.serve_forever()