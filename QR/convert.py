import pyqrcode
QRStr=input('Enter String/Link : ')
QRtr=QRStr
URL=pyqrcode.create(QRStr)
f=input('Enter Name of the File : ')
URL.png(f,scale=8)
