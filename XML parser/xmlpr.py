import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter location: ')
parms = dict()
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data.decode())
for t in tree:
    print(t)
