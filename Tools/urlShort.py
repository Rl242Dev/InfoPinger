import pyshorteners as pys

s = pys.Shortener()

url = str(input('Url : '))
print(s.tinyurl.short(url))