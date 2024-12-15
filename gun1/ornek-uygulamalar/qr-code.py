import qrcode

# QR kodu oluştur
def qr_kod_olustur(bilgi):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(bilgi)
    qr.make(fit=True)
    qr.make_image(fill="black", back_color="white").show()

veri = input("Gömmek istediğin veriyi girin:")

# QR kodu oluştur
qr_kod_olustur(veri)