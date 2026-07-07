import http.server
import socketserver
import socket

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return '127.0.0.1'

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    local_ip = get_local_ip()
    print(f"服务器已启动！")
    print(f"本地访问: http://localhost:{PORT}")
    print(f"局域网访问: http://{local_ip}:{PORT}")
    print(f"按 Ctrl+C 停止服务器")
    httpd.serve_forever()