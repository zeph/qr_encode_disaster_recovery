import pyqrcode
content_a = []
with open("chiave.armored") as f:
    content_a = f.readlines()
righe = len(content_a)
content1 = ''.join(content_a[:righe//2])
content2 = ''.join(content_a[righe//2:])
qr1 = pyqrcode.create(content1, version=29, error='M')
qr1.png("horn1.png", scale=6)
qr2 = pyqrcode.create(content2, version=29, error='M')
qr2.png("horn2.png", scale=6)
