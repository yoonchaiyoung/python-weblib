from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 성공
# GET / HTTP/1.1
# 200 OK
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)


if resp.status == 200:
    body = resp.read()
    print(body, type(body))


# 실패
# 404 Not Found
conn.request('GET', '/hello.html')
resp = conn.getresponse()
print(resp.status, resp.reason)

