import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

language_codes ="""
    Dil           Kodu
   ------        ------
   İngilizce      en
   İspanyolca     es
   Rusça          ru
   Portekizce     pt
   Endonezya      id
   Lehçe          pl
   İtalyanca      it
   Türkçe         tr"""

#Bu uygulamada, kullanıcının sesini kaydedecek ve bir dosyada saklayacağız. Bu nedenle, kaydın süresini ve kalitesini ayarlamamız gerekiyor:
duration = 5  # kayıt saniyeleri
sample_rate = 44100

lang_first=input("Hangi dil ile konusucaksin "+ language_codes + " : ")

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
    text = recognizer.recognize_google(audio, language=lang_first)
    print("Şunu söylediniz:", text)

#Şimdi tek yapmamız gereken olası hataları ele almak!
except sr.UnknownValueError:             # - Google gürültü veya sessizlik nedeniyle konuşmayı anlayamadığında
    print("Konuşma tanınamadı.")
except sr.RequestError as e:             # - İnternet bağlantısı yoksa veya API kullanılamıyorsa
    print(f"Hizmet hatası: {e}")

#🎯 Tebrikler! Mikrofonu dinleyen, sesi kaydeden, bir dosyaya kaydeden, konuşma transkripsiyonu için gönderen ve metin çıkışı yapan bir uygulama yazdınız! 
#Bu, herhangi bir sesli asistan, sohbet robotu ve hatta oyunlar için seslendirme gibi daha niş kullanımlarda kullanabileceğiniz temel bir özelliktir!

#--------------------------------------------------------------------------------------------------------------------------------------------------------

"""
from googletrans import Translator

try:
    translator = Translator()
    translated = translator.translate(text, dest='es')  # buradaki 'es' İspanyolca için bir koddur
    print("🌍 İspanyolca'ya çeviri:", translated.text)

except Exception as e:
    print("Hata Oldu!: " + str(e))
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------

from googletrans import Translator

lang = input("Hangi dile çevirmeliyim?" + language_codes + " : ")

def get_language_name(code):
    match code.lower().strip():
        case "en": return "İngilizce"
        case "es": return "İspanyolca"
        case "ru": return "Rusça"
        case "pt": return "Portekizce"
        case "id": return "Endonezya"
        case "pl": return "Lehçe"
        case "it": return "İtalyanca"
        case "tr": return "Türkçe"
        case _:    return "Bilinmeyen Dil"

try:
    dil_adi = get_language_name(lang)
    if dil_adi == "Bilinmeyen Dil":
        print("Hata Oldu!: Geçersiz dil seçtiniz.")
    else:
        translator = Translator()
        translated = translator.translate(text, dest=lang)
        print("🌍 " + dil_adi + " çeviri: " + translated.text)
except Exception as e:
    print("Hata Oldu!: " + str(e))