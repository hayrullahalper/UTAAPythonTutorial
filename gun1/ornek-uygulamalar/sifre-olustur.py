import random
import string

# Güvenli şifre oluşturma fonksiyonu
def guvenli_sifre_olustur():
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for i in range(12))
    return sifre

# Şifreyi oluştur ve yazdır
sifre = guvenli_sifre_olustur()
print(f"Yeni şifreniz: {sifre}")