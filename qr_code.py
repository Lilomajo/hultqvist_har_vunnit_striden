
import segno

qrcode = segno.make_qr("https://lilomajo.github.io/hultqvist_har_vunnit_striden/")

qrcode.save("QRcode.png",
light=None,
scale=10)



