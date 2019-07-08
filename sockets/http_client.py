"""HTTP Client"""
import http.client

conn = http.client.HTTPConnection('localhost', 80)
conn.request('GET', '/opencart')

r1 = conn.getresponse()

code_of_response = r1.status
print(code_of_response)

reason = r1.reason
print(reason)
headers_of_response = r1.headers

print(headers_of_response)

data = r1.read()
# return as bytes
print(data)

parsed = data.decode('utf-8')
parser = parsed.split(' ')
# return as list
print(parser)

conn.close()
