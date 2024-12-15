import requests

# IP Geolocation API anahtarı
api_key = 'write your api key here'  # Kendi API anahtarınızı buraya koyun

# Kullanıcının IP adresini öğren
ip_address = input("IP adresi girin: ")

# API URL'sine istek yap
url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"
response = requests.get(url)
data = response.json()

print(url)

# Konum bilgisini al
country = data['country_name']
city = data['city']
print(f"{ip_address} adresinin konumu: {city}, {country}")