# Basit hesap makinesi

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return x / y

print("İşlem Seçin:")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")
print("5.Cikis")

# Kullanıcıdan seçim al
secim = input("Seçiminizi yapın (1/2/3/4/5): ")

# Kullanıcıdan iki sayı al
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# Seçime göre işlemi yap
if secim == '1':
    print(toplama(sayi1, sayi2))
elif secim == '2':
    print(cikarma(sayi1, sayi2))
elif secim == '3':
    print(carpma(sayi1, sayi2))
elif secim == '4':
    print(bolme(sayi1, sayi2))
elif secim == '5':
    print("Çıkış yapıldı")
else:
    print("Geçersiz giriş!")