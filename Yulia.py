import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os


r = sr.Recognizer()

def record(ask = False):
     with sr.Microphone() as source:
         if ask:
             speak(ask)
         audio = r.listen(source)
         voice = ''
         try:
             voice = r.recognize_google(audio , language='tr-TR')
         except sr.UnknownValueError:
             speak('Tekrar Edermisin')
             print('Tekrar edermisin')
         except sr.RequestError:
             speak('Hata')
         return voice

def response(voice):
     if 'Yulya' in voice:
         speak('efendim patron')
     if 'nasılsın' in voice:
         speak('redqueen kadar canlıyım sen nasılsın')
     if 'iyiyim' in voice:
         speak ('iyi olmana sevindim patron')
     if 'Sen kimsin' in voice:
         speak('İsmim Yulia Zihin kurgumda ukraynalı bir asistanım bir yaşım veya vücudum yok')
     if 'saat kaç' in voice:
         speak(datetime.now().strftime('%H:%M:%S'))
     if 'araştır' in voice:
         search = record('Ne araştırmalıyım')
         url = 'https://google.com/search?q='+search
         webbrowser.get().open(url)
         speak(search + 'webde araştırılıyor')
     if 'tamamdır' in voice:
         exit(url)
     if 'müzik aç' in voice:
         youtube= 'https://youtu.be/wibFr7DbNfw'
         webbrowser.get().open(youtube)
         music = record('Elektronik bir şeyler çalıyorum')
     if 'kapat' in voice:
         exit(youtube)
     if 'film aç' in voice:
         snf = 'https://sinefy.net/'
         webbrowser.get().open(snf)
         movie = record('ne izlemek istersin')
     if 'valorant aç' in voice:
         os.startfile('C:\Riot Games\Riot Client\RiotClientServices.exe')
         game = record('valorant başlatılıyor iyi oyunlar')
     
      
def speak(string):
     tts = gTTS(string,lang='tr')
     rand = random.randint(1,10000)
     file = 'audio-'+str(rand)+'.mp3'
     tts.save(file)
     playsound(file)
     os.remove(file)

speak('Yulia dinlemede')
print('Yulia dinlemede')
time.sleep(1)
while 1:
     voice = record()
     print(voice)
     response(voice)