import time


# Zamanlayıcı ve yapılacaklar listesi
def zamanlayici_ve_yapilacaklar():
    # Yapılacaklar listesi
    yapilacaklar = []
    while True:
        print("\n1. Yeni görev ekle")
        print("2. Görevleri görüntüle")
        print("3. Görev tamamla")
        print("4. Zamanlayıcı başlat")
        print("5. Çık")

        secim = input("Bir seçenek girin: ")

        if secim == '1':
            görev = input("Yeni görev: ")
            yapilacaklar.append(görev)
        elif secim == '2':
            print("\nYapılacaklar Listesi:")
            for idx, görev in enumerate(yapilacaklar, 1):
                print(f"{idx}. {görev}")
        elif secim == '3':
            index = int(input("Tamamlanan görev numarasını girin: ")) - 1
            yapilacaklar.pop(index)
            print("Görev tamamlandı!")
        elif secim == '4':
            süre = int(input("Çalışma süresini saniye olarak girin: "))
            print(f"Zamanlayıcı başlatılıyor {süre} saniye boyunca...")
            time.sleep(süre)
            print("Zamanlayıcı tamamlandı!")
        elif secim == '5':
            break
        else:
            print("Geçersiz seçenek.")


# Uygulamayı başlat
zamanlayici_ve_yapilacaklar()