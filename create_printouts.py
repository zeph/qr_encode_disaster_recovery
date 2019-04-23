import pyqrcode
content = ""
c_limit = 512

with open("chiave.armored") as f:
    content = ''.join(f.readlines())

c_count = len(content)/c_limit

for i in xrange(0, c_count):
    chunk = content[i*c_limit:c_limit]
    qr = pyqrcode.create(chunk, version=21, error='L')
    qr.png('chunk{0}.png'.format(i), scale=6)
