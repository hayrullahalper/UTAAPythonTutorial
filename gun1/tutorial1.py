# Python'a Giriş: Temel ve İleri Düzey Konular - Eğitim Materyali

# Adım 1: Değişkenler ve Veri Tipleri

# Python'da değişkenler, bir değeri tutan isimlerdir.
# Python, dinamik bir dil olduğu için, değişkenler türünü otomatik olarak belirler.
# Bu özellik sayesinde tip tanımlaması yapmadan değişkenler kullanılabilir.

# Örnek 1: Temel Değişkenler
x = -10        # x, bir integer (tam sayı) değeri tutar
y = 5.5       # y, bir float (ondalıklı sayı) değeri tutar
name = "Ali"  # name, bir string (metin) değeri tutar
aktif_mi = True  # is_active, bir boolean (True/False) değeri tutar

# Değişkenlerin değerlerini ekrana yazdıralım
print("x:", x * 2)
print("y:", y)
print("name:", name)
print("is_active:", aktif_mi)

# Python veri tipleri:
# - int: Tam sayılar
# - float: Ondalıklı sayılar
# - str: Metin (string)
# - bool: True veya False
# - list: Liste -> ["ali","veli","deli"]
# - tuple: Değiştirilemez liste (1,2,3)
# - dict: Sözlük (anahtar-değer çiftleri)

# Adım 2: Veri Tipi Dönüşümleri

# Python'da veri tipi dönüşümleri oldukça basittir.
# String'leri sayılara, sayıları string'lere dönüştürebiliriz.

# Örnek 2: String'i Integer'a Dönüştürme
a = "100"      # a bir string (metin) değeri
b = int(a)

print("\nString'ten Integer'a Dönüşüm:")
print("b:", b)  # 100

# Örnek 3: Integer'ı Float'a Dönüştürme
c = float(b)   # b'yi float'a dönüştürdük 100.0
print("\nInteger'tan Float'a Dönüşüm:")
print("c:", c)  # 100.0

# Örnek 4: Float'ı String'e Dönüştürme
d = str(c)     # c'yi string'e dönüştürdük
print("\nFloat'tan String'e Dönüşüm:")
print("d:", d)  # "100.0"

# Adım 3: Koşul İfadeleri (if-else)

# Python'da koşul ifadeleri, programın bir bölümünü koşullara göre çalıştırmamızı sağlar.
# Koşul, doğruysa 'if' bloğu çalışır, yanlışsa 'else' bloğu çalışır.

# Örnek 5: Yaş Kontrolü
age = int(input("\nYaşınızı girin: "))

if age >= 18:
    print("Hoş geldiniz! 18 yaş ve üzeri bir bireysiniz.")
else:
    print("Üzgünüz, 18 yaşından küçük olduğunuz için erişiminiz kısıtlanmıştır.")

# Örnek 6: Girilen Sayının Pozitif, Negatif veya Sıfır Olup Olmadığını Kontrol Etme
number = int(input("\nBir sayı girin: "))

if number > 0:
    print("Sayı pozitiftir.")
elif number < 0:
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")

# Adım 4: Döngüler (for, while)

# Döngüler, bir işlemi belirli sayıda veya bir koşul sağlanana kadar tekrar yapmamıza olanak tanır.
# 'for' döngüsü, belirli bir koleksiyon üzerinden geçerken kullanılır.
# 'while' döngüsü ise bir koşul doğru olduğu sürece çalışır.

# Örnek 7: For Döngüsü ile Liste Üzerinde İşlem Yapmak
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0

for num in numbers:
    sum_of_numbers = sum_of_numbers + num  # sum_of_numbers'a num'yi ekliyoruz

print("\nFor Döngüsü ile Liste Elemanlarının Toplamı:", sum_of_numbers)

# Örnek 8: Range Fonksiyonu ile Sayılar Üzerinde Döngü
print("\n1'den 10'a kadar olan sayılar:")
for i in range(1, 11):  # range(1, 11) 1 ile 10 arasındaki sayıları döndüren bir fonksiyondur
    print(i)

# range(1,11) = [1,2,3,4,...,10]

# Örnek 9: While Döngüsü ile Koşula Bağlı Girdi Almak
counter = 0

while counter < 3:
    user_input = input("\nBir şeyler yazın ('q' ile çıkabilirsiniz): ")
    if user_input == 'q':
        print("Çıkılıyor...")
        break  # 'q' tuşuna basıldığında döngüden çık
    else:
        print(f"Girdiğiniz metin: {user_input}")
    counter += 1

# Adım 5: Fonksiyonlar

# Fonksiyonlar, bir işlemi tekrar kullanabilmek için tanımlanan yapılardır.
# Python'da bir fonksiyon, `def` anahtar kelimesiyle tanımlanır.

# Örnek 10: Basit Fonksiyon Tanımlama
def selamla(name):
    """
    Bu fonksiyon, verilen ismi alır ve kullanıcıyı selamlar.
    """
    print(f"Merhaba, {name}!")

# Fonksiyonu çağırma
selamla("Ali")  # "Ali" isminde bir kullanıcıyı selamlayacağız.

# Örnek 11: Fonksiyon ile Hesaplama
def add_numbers(a, b):
    """
    Bu fonksiyon, iki sayıyı toplar ve sonucu döndürür.
    """
    return a + b

# Fonksiyonu çağırarak iki sayıyı toplayalım
result = add_numbers(10, 20)
print("\nToplam:", result)  # 30

# Örnek 12: Parametreli Fonksiyon ile Çift veya Tek Sayı Kontrolü
def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} bir çift sayıdır.")
    else:
        print(f"{number} bir tek sayıdır.")

check_even_or_odd(15)  # "15 bir tek sayıdır."
check_even_or_odd(10)  # "10 bir çift sayıdır."

# Adım 6: Listeler

# Listeler, birden fazla öğeyi sıralı bir şekilde saklayan veri yapılarıdır.
# Liste elemanları indekslerle erişilebilir.

# Örnek 13: Liste Kullanımı
fruits = ["elma", "armut", "muz", "çilek"]

# Listeye yeni bir eleman ekleyelim
fruits.append("karpuz")
# ["elma", "armut", "muz", "çilek", "karpuz"]

fruits.remove("muz")
# ["elma", "armut", "çilek", "karpuz"]



# Liste elemanlarını sırasıyla yazdıralım
print("\nListe Elemanları:")
for fruit in fruits:
    print(fruit)

# Liste elemanlarına indeksle erişelim
print("\nListenin 3. elemanı (indeks 2):", fruits[2])

# Adım 7: Sözlükler (Dictionaries)

# Sözlükler, anahtar-değer çiftlerinden oluşur ve veriye anahtar ile erişim sağlar.
# Anahtarlar benzersiz olmalıdır.

# Örnek 14: Sözlük Kullanımı
user_info = {
    "isim": "Ali",
    "yaş": 25,
    "meslek": "Yazılımcı"
}

# Sözlükten bir değeri alalım
print("\nKullanıcı Bilgileri:")
print("İsim:", user_info["isim"])
print("Yaş:", user_info["yaş"])
print("Meslek:", user_info["meslek"])

# Adım 8: Dosya İşlemleri

# Python, dosya okuma ve yazma işlemlerini çok kolay bir şekilde yapabiliriz.
# Dosya açmak, okuma ve yazma işlemleri oldukça basittir.

# Örnek 15: Dosyaya Yazma
with open("example.txt", "w") as file:
    file.write("Python'a Giriş!\nBu bir dosya yazma örneğidir.")

# Örnek 16: Dosyayı Okuma
with open("example.txt", "r") as file:
    content = file.read()
    print("\nDosyadaki içerik:")
    print(content)

# Adım 9: Hata Yönetimi (Try-Except)

# Python'da try-except blokları, hata yönetimi için kullanılır.
# Hataları düzgün bir şekilde yakalar ve işleyebiliriz.

# Örnek 17: Hata Ayıklama

try:
    number = int(input("\nBir sayı girin: "))
    result = 10 / number  # 0 ile bölme hatası alabiliriz
    print(f"Sonuç: {result}")
except ZeroDivisionError:
    print("Hata: Sıfıra bölme hatası!")
except ValueError:
    print("Hata: Geçersiz giriş, lütfen geçerli bir sayı girin.")
except Exception as e:
    print(f"Bilinmeyen bir hata oluştu: {e}")

# Adım 10: Listelerde ve Sözlüklerde İleri Seviye İşlemler

# Liste ve sözlüklerle daha karmaşık işlemler yapmak mümkün.

# Örnek 18: Listeyi Sıralama
numbers = [5, 1, 8, 4, 2]
numbers.sort()  # Listeyi küçükten büyüğe sıralar
print("\nSıralanmış Liste:", numbers)

# Örnek 19: Sözlükte Anahtarları ve Değerleri Listeleme
person = {
    "isim": "Veli",
    "yaş": 30,
    "meslek": "Mühendis",
    "arkadaslar": ["ali","veli"]
}

print("\nSözlük Anahtarları:", list(person.keys()))
print("Sözlük Değerleri:", list(person.values()))


### Adım 11: Python'da Hazır Kütüphaneler ve Paketler
# Python, zengin bir standart kütüphane setine sahiptir ve aynı zamanda harici paketlerle geliştirilebilir.

# Örnek 20: Matematik Kütüphanesi (math)
import math

# Bir sayının karekökünü alalım
sayi = 16
karekok = math.sqrt(sayi)
print(f"\nSayının Karekökü: {karekok}")

# Bir açı değerinin sinüsünü alalım (radyan cinsinden)
aci = math.radians(30)  # Dereceyi radyana çeviriyoruz
sinus = math.sin(aci)
print(f"30 Derecenin Sinüsü: {sinus}")

# Örnek 21: Rastgele Sayılar (random)
import random

# 1 ile 100 arasında rastgele bir sayı üretelim
rastgele_sayi = random.randint(1, 100)
print(f"\nRastgele Üretilen Sayı: {rastgele_sayi}")

# Bir listeden rastgele bir eleman seçelim
liste = ['Python', 'Java', 'C++', 'JavaScript']
rastgele_secim = random.choice(liste)
print(f"Listeden Rastgele Seçim: {rastgele_secim}")

# Örnek 22: Tarih ve Saat (datetime)
from datetime import datetime

# Şu anki tarih ve saati öğrenelim
simdi = datetime.now()
print(f"\nŞu Anki Tarih ve Saat: {simdi}")

# Sadece tarihi alalım
bugunun_tarihi = simdi.date()
print(f"Bugünün Tarihi: {bugunun_tarihi}")

# Örnek 23: Sistem İşlemleri (os)
import os

# Şu anki çalışma dizinini öğrenelim
calisma_dizini = os.getcwd()
print(f"\nÇalışma Dizini: {calisma_dizini}")

# Örnek 24: Zaman Ölçümleri (time)
import time

print("\nBir zaman ölçümü başlatılıyor...")
time.sleep(2)  # 2 saniye bekler
print("2 saniye sonra bu mesaj görüntülenir!")

# Örnek 27: Matplotlib ile Grafik Çizimi
# Matplotlib, grafik ve veri görselleştirme için kullanılır.
import matplotlib.pyplot as plt

# Bir basit grafik çizelim
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, marker='o')
plt.title("X ve Y'nin Grafiği")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.show()