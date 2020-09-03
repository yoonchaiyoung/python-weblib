from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

port = 8888
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        result = urlparse(self.path)

        if result.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('<h1>메인페이지 입니다.<h1>'.encode('utf-8'))
        elif result.path == '/board':
            params = parse_qs(result.query)
            print(result.path)
            print(params)

            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('<h1>게시판입니다.<h1>'.encode('utf-8'))
        elif result.path == '/user':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('<h1>안녕하세요<h1>'.encode('utf-8'))
        elif result.path == '/favicon.ico':
            pass





httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
#  모든 ip에서 접근하는 요청 다 받겠다   포트
print(f'Server Running on Port {port}')
httpd.serve_forever()

# 출력값 : Server Running on Port 8888


