from urllib import request
from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
http_response = urlopen('https://www.example.com')
body = http_response.read()
html = body.decode("utf-8")
print(html)

http_response = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
body = http_response.read()
html = body.decode("cp949")
print(html)

from urllib.request import urlopen

http_response = urlopen('https://www.example.com?a=10&b=20')  # GET 방식은 데어터가 url에 달려있음
body = http_response.read()
html = body.decode("utf-8")
print(html)

# POST
data = {
    'id': 'kickscar',
    'pw': '1234'
}

data = urlencode(data).encode('utf-8')

request('https://nid.naver.com/nidlogin.login', data)
request.add_header('Content-Type', 'text/html')

urlopen(request)

data = {
    'id': 'kickscar',
    'pw': '1234'
}

data = urlencode(data).encode('utf-8')

request('https://www.example.com', data)
request.add_header('Content-Type', 'text/html')

urlopen(request)
