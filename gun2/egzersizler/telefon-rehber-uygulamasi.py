phone_book = {}

while True:
    print("\n1. Yeni kişi ekle\n2. Rehberi görüntüle\n3. Numara ara\n4. Çıkış")
    choice = input("Seçiminiz: ")

    if choice == "1":
        name = input("İsim: ")
        number = input("Numara: ")
        phone_book[name] = number
        print(name, " rehbere eklendi.")
    elif choice == "2":
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    elif choice == "3":
        name = input("Kimi arıyorsunuz? ")

        if name in phone_book:
            print(f"{name}: {phone_book.get(name, 'Kayıtlı değil.')}")
        else:
            print(name, " rehberde bulunmuyor.")
    elif choice == "4":
        break
    else:
        print("Geçersiz seçim!")