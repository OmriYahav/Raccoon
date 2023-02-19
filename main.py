import requests

IpApi = requests.get('http://ip-api.com/json/')
weather = requests.get('http://wttr.in')
cryptoRate = requests.get('http://rate.sx')
Ipconfig = requests.get('http://ifconfig.io/ip')

IP = IpApi.json()
print(IpApi.text)
print(weather.text)
print(cryptoRate.text)
print(Ipconfig.text)


# print(IP)
# print("Query:",IP['status'])
# print("IP:",IP['query'])
# print("ISP:",IP['as'])
# print("AS:",IP['isp'])
# print("Country:",IP['country'])
# print("Region Name:",IP['regionName'])
# print("City:",IP['city'])
# print("Latitude:",IP['lat'])
# print("Longtitude:",IP['lon'])
# print("Country:",IP['country'])
