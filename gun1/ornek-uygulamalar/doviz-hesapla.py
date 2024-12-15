import requests

# Döviz kuru hesaplayıcı
def doviz_kuru_hesapla():
    # Kullanıcıdan döviz türlerini al
    base_currency = input("Başlangıç para birimini girin (örneğin: USD, EUR): ")
    target_currency = input("Hedef para birimini girin (örneğin: TRY, EUR): ")
    amount = float(input("Dönüştürmek istediğiniz miktarı girin: "))

    # Döviz kurları API'sini kullanarak veriyi al
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    print(url)

    response = requests.get(url)
    data = response.json()

    if target_currency in data['rates']:
        conversion_rate = data['rates'][target_currency]
        converted_amount = amount * conversion_rate
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print(f"Geçersiz hedef para birimi: {target_currency}")

# Döviz dönüşümünü başlat
doviz_kuru_hesapla()