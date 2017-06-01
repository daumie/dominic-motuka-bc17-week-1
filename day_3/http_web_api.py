"""Module docstring"""
import http.client
import requests
from pprint import pprint

conn = http.client.HTTPConnection("www.open-notify.com")
conn.request("HEAD", "/")
res = conn.getresponse()
response = requests.get("http://api.open-notify.org/iss-now.json")
response.json()

if res.status == 500:
    print("INTERNAL SERVER ERROR")
elif res.status == 404:
    print("THE PAGE CANNOT BE FOUND")
elif res.status == 403:
    print("UNAUTHORIZED ACCESS")
elif res.status == 400:
    print("BAD REQUEST")
elif res.status == 200:
    print("status OK")
elif res.status == 301:
    print("OK , WELCOME TO THE INTERNATIONAL SPACE STATION ")
    print("Current posisition of the International Space Station Satelite is :\n")
    pprint(response.json())
else:
    print("unable to ACCESS data")