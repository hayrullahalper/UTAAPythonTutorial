import requests

# CoinGecko API URL'si
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
response = requests.get(url)
data = response.json()

# Bitcoin ve Ethereum fiyatlarını al
bitcoin_price = data['bitcoin']['usd']
ethereum_price = data['ethereum']['usd']

print(f"Bitcoin Fiyatı: ${bitcoin_price}")
print(f"Ethereum Fiyatı: ${ethereum_price}")