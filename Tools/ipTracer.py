import urllib.request
import subprocess as sp

#31.36.137.199

ips = []

ipp = str(input('IP : '))
ips.append(ipp)

for ip in ips:
        with urllib.request.urlopen("https://geolocation-db.com/jsonp/"+ip) as url:
                data = url.read().decode()
                data = data.split("(")[1].strip(")")
                print(data)
                