import pyqrcode
import png
link = "https://hacktoberfest.com/"
qr_code = pyqrcode.create(link)
qr_code.png("wbpage.png", scale=5)
