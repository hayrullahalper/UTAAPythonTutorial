import requests

# Hava Durumu Uygulaması
def hava_durumu(sehir):
    api_key = "write your api key here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric"

    print(url)

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"{sehir} için Hava Durumu:")
        print(f"Sıcaklık: {data['main']['temp']}°C")
        print(f"Hava: {data['weather'][0]['description']}")
    else:
        print("Hava durumu verisi alınamadı.")

# Kullanıcıdan şehir ismi al
sehir = input("Hava durumunu öğrenmek için şehir ismini girin: ")

# Hava durumunu göster
hava_durumu(sehir)