# Not hesaplama sistemi
def not_hesaplama():
    dersler = {}

    while True:
        ders_adı = input("Ders adı girin (Çıkmak için 'q' girin): ")
        if ders_adı.lower() == 'q':
            break
        not_ = float(input(f"{ders_adı} dersinin notunu girin: "))
        dersler[ders_adı] = not_

    ortalama = sum(dersler.values()) / len(dersler)
    print("\nDers Notları:")
    for ders, not_ in dersler.items():
        print(f"{ders}: {not_}")

    print(f"Toplam Ortalama: {ortalama}")


# Not hesaplama fonksiyonunu başlat
not_hesaplama()