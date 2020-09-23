import pyqrcode

QRString = 'https://github.com/Umka6/portfolio/blob/master/index.html'
url = pyqrcode.create(QRString)
url.png('sait.png', scale=8)
