from pytube import YouTube

# Video URL'si
video_url = input("YouTube Video URL'sini girin: ")

# Video İndirme
try:
    yt = YouTube(video_url)
    print(f"Video Başlığı: {yt.title}")

    # En yüksek çözünürlükte video indirme
    stream = yt.streams.get_highest_resolution()
    stream.download()

    print(f"Video başarıyla indirildi: {yt.title}.mp4")
except Exception as e:
    print(f"Hata: {e}")