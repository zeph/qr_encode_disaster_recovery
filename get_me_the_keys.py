import qrtools
qr1 = qrtools.QR()
qr2 = qrtools.QR()
qr1.decode("horn1.png")
print qr1.data,
qr2.decode("horn2.png")
print qr2.data
