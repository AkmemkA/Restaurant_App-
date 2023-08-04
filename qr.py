import qrcode

image = qrcode.make("https://jufc.ru")
image.save("qr.png")