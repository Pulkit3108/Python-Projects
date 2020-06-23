import contextlib
import urllib.request, urllib.parse, urllib.error

def make_tiny(url):
	request_url = ('http://tinyurl.com/api-create.php?' + 
	urllib.parse.urlencode({'url':url}))
	with contextlib.closing(urllib.request.urlopen(request_url)) as response:
		return response.read().decode('utf-8')

s=input("Enter The URL : ")
x=make_tiny(s)
print("Result :",x)


