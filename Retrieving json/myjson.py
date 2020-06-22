import urllib.request, urllib.parse, urllib.error
import ssl
import json



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter location: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
info = json.loads(data)
print(info)
