import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

#Bu uygulamada, kullanıcının sesini kaydedecek ve bir dosyada saklayacağız. Bu nedenle, kaydın süresini ve kalitesini ayarlamamız gerekiyor:
duration = 5  # kayıt saniyeleri
sample_rate = 44100

#Kurulum tamamlandıktan sonra, kullanıcıya kaydı başlattığımızı bildirip sesini kaydetmemiz gerekir:
print("Şimdi konuşun...")
recording = sd.rec(
  int(duration * sample_rate), # kaydedilecek örnek sayısı
  samplerate=sample_rate,      # örnekleme hızı
  channels=1,                  # 1, mono kayıt anlamına gelir.
  dtype="int16")               # kayıtlı örnekler için veri türü
sd.wait()  # kayıt bitene kadar beklemek

#Kayıt tamamlandığında, bir dosyaya kaydedebiliriz:
wav.write("output.wav", sample_rate, recording)
print("Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")

#Ve şimdi önemli kısım: speech_recognition kullanarak dosyayı yükleyelim ve tanıma için hazırlayalım:
recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source) #veri dijital veri oldu

#speech_recognition, Python'da kullanılabilen basit ve popüler bir konuşma tanıma kütüphanesidir. 
#Ücretsiz Google Konuşma Tanıma API'sı da dahil olmak üzere farklı "motorlar" (konuşma tanıma hizmetleri) kullanarak konuşmayı metne dönüştürmemizi sağlar.

#Ses dosyasını Google Konuşma Tanıma API'sına göndererek transkripsiyonlu metni alalım:
try:
    text = recognizer.recognize_google(audio, language="tr")
    print("Şunu söylediniz:", text)

#Şimdi tek yapmamız gereken olası hataları ele almak!
except sr.UnknownValueError:             # - Google gürültü veya sessizlik nedeniyle konuşmayı anlayamadığında
    print("Konuşma tanınamadı.")
except sr.RequestError as e:             # - İnternet bağlantısı yoksa veya API kullanılamıyorsa
    print(f"Hizmet hatası: {e}")

#🎯 Tebrikler! Mikrofonu dinleyen, sesi kaydeden, bir dosyaya kaydeden, konuşma transkripsiyonu için gönderen ve metin çıkışı yapan bir uygulama yazdınız! 
#Bu, herhangi bir sesli asistan, sohbet robotu ve hatta oyunlar için seslendirme gibi daha niş kullanımlarda kullanabileceğiniz temel bir özelliktir!
