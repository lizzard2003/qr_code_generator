import pyqrcode
import png
from pyqrcode import QRCode
profile = "http://linkedin.com/in/liz-de-la-rosa/"
url = pyqrcode.create(profile)
url.svg("qr_code.svg",scale =10)
url.png("LinkedIn_qr_code.png", scale=10) 
print(url.terminal(quiet_zone=1))
