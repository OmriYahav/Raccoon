import requests

IpApi = requests.get('http://ip-api.com/json/')
IP = IpApi.json()

# print(IP)
print("Query:",IP['status'])
print("IP:",IP['query'])
print("ISP:",IP['as'])
print("AS:",IP['isp'])
print("Country:",IP['country'])
print("Region Name:",IP['regionName'])
print("City:",IP['city'])
print("Latitude:",IP['lat'])
print("Longtitude:",IP['lon'])
print("Country:",IP['country'])
