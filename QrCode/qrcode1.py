import qrcode
img = qrcode.make("https://www.linkedin.com/in/neelvaria/")
img.save("qrcode/qrcode.png")