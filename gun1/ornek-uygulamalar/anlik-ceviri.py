import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Çeviri için bir Translator nesnesi oluştur
translator = Translator()

# Sesli yanıt için pyttsx3 motoru ayarla
engine = pyttsx3.init()

# SpeechRecognition için bir recognizer oluştur
recognizer = sr.Recognizer()

print("Anlık çeviri için konuşmaya başlayabilirsiniz (çıkmak için Ctrl+C)")

while True:
    try:
        # Mikrofondan ses yakalama
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Ortam gürültüsünü ayarla
            print("Dinliyor...")
            audio = recognizer.listen(source, timeout=5)  # 5 saniyelik dinleme süresi

            # Sesi metne dönüştür
            print("Metne dönüştürülüyor...")
            speech_text = recognizer.recognize_google(audio, language="tr-TR")  # Türkçe giriş
            print(f"Söylediğiniz: {speech_text}")

            # Metni İngilizceye çevir
            translation = translator.translate(speech_text, src="tr", dest="en")
            print(f"Çeviri: {translation.text}")

            # Çeviriyi sesli olarak oynat
            engine.say(translation.text)
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Ne söylediğinizi anlayamadım, lütfen tekrar deneyin.")
    except sr.RequestError as e:
        print(f"Bir hata oluştu: {e}")
    except KeyboardInterrupt:
        print("\nÇıkış yapılıyor...")
        break