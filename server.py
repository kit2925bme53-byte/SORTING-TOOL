from http.server import BaseHTTPRequestHandler, HTTPServer
import json

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


class RequestHandler(BaseHTTPRequestHandler):

    # ✅ THIS FIXES YOUR ERROR
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path == "/sort":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            numbers = data["numbers"]
            result = bubble_sort(numbers)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")  # ✅ REQUIRED
            self.end_headers()

            self.wfile.write(json.dumps({"result": result}).encode())


def run():
    server = HTTPServer(("localhost", 8000), RequestHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()


if __name__ == "__main__":
    run()