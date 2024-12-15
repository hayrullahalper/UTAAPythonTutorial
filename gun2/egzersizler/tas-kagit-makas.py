import random

# Kullanıcıdan giriş al
print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
kullanici_secimi = input("Taş, Kağıt ya da Makas seçin: ").lower()

# Bilgisayar rastgele seçim yapar
secenekler = ["taş", "kağıt", "makas"]
bilgisayar_secimi = random.choice(secenekler)

print(f"Bilgisayarın Seçimi: {bilgisayar_secimi}")

# Kazananı belirle
if kullanici_secimi == bilgisayar_secimi:
    print("Berabere!")
elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or \
     (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
     (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt"):
    print("Tebrikler, kazandınız!")
else:
    print("Kaybettiniz!")