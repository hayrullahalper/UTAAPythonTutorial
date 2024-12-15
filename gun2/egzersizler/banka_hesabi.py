class BankaHesabi:
    def __init__(self, isim, bakiye=0):
        self.isim = isim
        self.bakiye = bakiye

    def bakiye_goruntule(self):
        print(f"{self.isim} Hesabınızın Bakiyesi: {self.bakiye} TL")

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL hesabınıza yatırıldı.")
        else:
            print("Yatırılacak miktar sıfırdan büyük olmalıdır.")

    def para_cek(self, miktar):
        if miktar > 0:
            if miktar <= self.bakiye:
                self.bakiye -= miktar
                print(f"{miktar} TL hesabınızdan çekildi.")
            else:
                print("Yetersiz bakiye!")
        else:
            print("Çekilecek miktar sıfırdan büyük olmalıdır.")



isim = input("Hesabınızın adını girin: ")
hesap = BankaHesabi(isim)

while True:
    print("\n--- Banka Hesap Yönetimi ---")
    print("1. Bakiye Görüntüle")
    print("2. Para Yatır")
    print("3. Para Çek")
    print("4. Çıkış")

    secim = input("Bir işlem seçin (1/2/3/4): ")

    if secim == '1':
        hesap.bakiye_goruntule()
    elif secim == '2':
        miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
        hesap.para_yatir(miktar)
    elif secim == '3':
        miktar = float(input("Çekmek istediğiniz miktarı girin: "))
        hesap.para_cek(miktar)
    elif secim == '4':
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")