import pyshorteners as ps
url=input('Enter Your Link : ')
u=ps.Shortener().tinyurl.short(url)
print('Tiny URL : ',u)
