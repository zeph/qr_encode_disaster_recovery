import qrcode
import qrcode.image.svg

method = 'basic'
chunks = 3

content_a = ""
with open("chiave.armored") as f:
    content_a = f.readlines()

if method == 'basic':
    # Simple factory, just a set of rects.
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (also just a set of rects)
    factory = qrcode.image.svg.SvgFragmentImage
else:
    # Combined path factory, fixes white space that may occur when zooming
    factory = qrcode.image.svg.SvgPathImage

cs = len(content_a)//chunks
for i in range(0, chunks):
    img = qrcode.make(
        ''.join(content_a[cs*i:cs*(i+1)]),
        image_factory=factory)
    img.save("chunk{0}.svg".format(i), "SVG")