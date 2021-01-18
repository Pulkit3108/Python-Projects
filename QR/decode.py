import cv2 as cv
r=input('Enter Path Of The File : ')
im = cv.imread(r)
det = cv.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(im)
print(retval)
