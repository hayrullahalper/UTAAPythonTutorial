# Bu dosyada sınıflar, özellikler (attributes) ve metotlarla (methods) ilgili
# temel bilgileri öğrenip, basit örnekler ve uygulamalar yapacağız.

# 1 - TEMEL SINIF TANIMLAMA
# Bir sınıf nasıl tanımlanır ve nesne (object) nasıl oluşturulur?
class Ogrenci:
    # Sınıf oluşturulduğunda ilk çalışacak metot (__init__)
    def __init__(self, isim, yas):
        self.isim = isim  # Öğrencinin adı
        self.yas = yas    # Öğrencinin yaşı

# Nesne oluşturma
ogr1 = Ogrenci("Ahmet", 20)
ogr2 = Ogrenci("Ayşe", 22)

# Özelliklere erişim
print("Öğrenci 1'in adı:", ogr1.isim)
print("Öğrenci 2'nin yaşı:", ogr2.yas)

print("\n" + "-"*40 + "\n")

# 2 - SINIF METOTLARI
# Sınıfa işlemler yaptırmak için metotlar tanımlayabiliriz.
class Ogrenci:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    # Selam veren bir metot
    def selam_ver(self):
        return f"Merhaba, benim adım {self.isim} ve {self.yas} yaşındayım."

# Yeni bir nesne oluşturalım ve metodu çağıralım
ogr1 = Ogrenci("Ali", 19)
print(ogr1.selam_ver())

print("\n" + "-"*40 + "\n")

# 3 - GÜNLÜK HAYATTAN ÖRNEKLER
# Şimdi daha anlamlı bir örnek yapalım: Bir banka hesabı simülasyonu

class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye=0):
        self.hesap_sahibi = hesap_sahibi  # Hesap sahibinin adı
        self.bakiye = bakiye              # Hesap bakiyesi (varsayılan 0)

    # Para yatırma işlemi
    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{miktar} TL yatırıldı. Güncel bakiye: {self.bakiye} TL")

    # Para çekme işlemi
    def para_cek(self, miktar):
        if miktar > self.bakiye:
            print("Yetersiz bakiye!")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Güncel bakiye: {self.bakiye} TL")

# Kullanım örneği
hesap = BankaHesabi("Mehmet", 500)  # Mehmet'in 500 TL bakiyesi var
hesap.para_yatir(200)  # 200 TL yatır
hesap.para_cek(100)    # 100 TL çek
hesap.para_cek(700)    # Yetersiz bakiye uyarısı

print("\n" + "-"*40 + "\n")

# 4 - KÜTÜPHANE YÖNETİMİ
# Kütüphane uygulaması ile birden fazla sınıfı nasıl kullanabileceğimizi görelim.

class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad       # Kitap adı
        self.yazar = yazar # Kitap yazarı

    # Kitap bilgilerini göstermek için bir metot
    def bilgi_goster(self):
        return f"Kitap: {self.ad}, Yazar: {self.yazar}"


class Kutuphane:
    def __init__(self):
        self.kitaplar = []  # Kütüphane içindeki kitaplar

    # Kitap ekleme
    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"{kitap.ad} kütüphaneye eklendi!")

    # Kitapları listeleme
    def kitaplari_listele(self):
        print("\nKütüphanedeki kitaplar:")
        for kitap in self.kitaplar:
            print(kitap.bilgi_goster())

# Kullanım
k1 = Kitap("1984", "George Orwell")
k2 = Kitap("Sefiller", "Victor Hugo")

kutuphane = Kutuphane()
kutuphane.kitap_ekle(k1)
kutuphane.kitap_ekle(k2)
kutuphane.kitaplari_listele()