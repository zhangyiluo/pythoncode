#coding=utf-8
import urllib.request

# This code test in python3.8 pass.
# Attention! urllib is diffenent from low version urllib2
def getData():
    url = 'https://example.com'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    print(type(req))
    #html = urllib.request.urlopen(req).read()
    #print(html)

def main():
    datalist=getData()
 
main()
