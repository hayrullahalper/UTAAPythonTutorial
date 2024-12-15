import random


# Sayı tahmin etme oyunu
def sayi_tahmin_et():
    hedef_sayi = random.randint(1, 100)
    print("1 ile 100 arasında bir sayı tuttum. Tahmin et!")

    while True:
        tahmin = int(input("Tahmininizi girin: "))

        if tahmin < hedef_sayi:
            print("Daha büyük bir sayı girin!")
        elif tahmin > hedef_sayi:
            print("Daha küçük bir sayı girin!")
        else:
            print("Tebrikler, doğru tahmin ettiniz!")
            break


# Oyun başlat
sayi_tahmin_et()