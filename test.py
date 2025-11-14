from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 9630

class Handler(SimpleHTTPRequestHandler):
    print("prabhash")
    pass

if __name__ == "__main__":
    server = HTTPServer(("", PORT), Handler)
    print(f"HTTP server running on port {PORT}")
    server.serve_forever()

