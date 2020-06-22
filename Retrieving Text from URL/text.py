import urllib.request, urllib.parse, urllib.error
f=input("Enter URL to fetch text : ")
x = urllib.request.urlopen(f)
for i in x:
    print(i.decode().strip())
