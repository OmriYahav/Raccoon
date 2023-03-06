import requests

IpApi = requests.get('http://ip-api.com/json/')
IP = IpApi.json()
for i, value in IP.items():
     print(f"\t{i.upper()}: {value}")

