import urlexpander

url = str(input('Url : ')) # https/http

if len(url) < 2:
    print('Invalid Input')
    quit()
else:
    urlE = urlexpander.expand(url)
    print('')
    print(urlE)

