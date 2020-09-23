import pyqrcode

QRString = 'https://umka6.github.io/porfolio/'
url = pyqrcode.create(QRString)
url.png('sait.png', scale=8)
