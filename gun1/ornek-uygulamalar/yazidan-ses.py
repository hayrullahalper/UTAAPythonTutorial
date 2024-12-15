from gtts import gTTS

# Metni sese dönüştürme
text = "Python ile yazıyı sese dönüştürüyorum."
tts = gTTS(text, lang='tr')

# Ses dosyasını kaydet ve çal
tts.save("ses.mp3")
print("Ses dosyası oluşturuldu! Lütfen 'ses.mp3' dosyasını açarak dinleyin.")