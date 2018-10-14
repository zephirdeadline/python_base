import http.server
import os

PORT = 8001

"""
Address is localhost
"""
ADDRESS = ("", PORT)

server = http.server.HTTPServer
"""
CGI is to run python script, To only serve Html, use simpleHTTPRequestHandler(source: root folder)
"""
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(ADDRESS, handler)

print("server running...")
httpd.serve_forever()
