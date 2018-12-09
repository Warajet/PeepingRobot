import requests
import time

url = "http://192.168.0.118:5000/yz_json"

while(True):
    r = requests.get(url)

    print(r.status_code) # 200
    print(r.headers['content-type']) # 'application/json; charset=utf8'
    print(r.encoding) # 'utf-8'
    print(r.text) # u'{"type":"User"...'
    #print(r.json()) #{u'private_gists': 419, u'total_private_repos': 77, ...}
    time.sleep(0.1)
