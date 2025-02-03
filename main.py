import pyttsx3 as p 
import speech_recognition as sr
from selenium_main import InfoW
from YouTube_auto import Music

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello Sir I am your voice assistent. How are you")

with sr.Microphone() as source:
  r.energy_threshold = 10000
  r.adjust_for_ambient_noise(source,1.2)
  print("listening")
  audio =  r.listen(source)
  text = r.recognize_google(audio)
  print(text)

  if "how" and "about" and "you" in text:
     speak("i am good sir")
     speak("i am help you?")


with sr.Microphone() as source:
   r.energy_threshold = 10000
   r.adjust_for_ambient_noise(source,1.2)
   print("listening...")
   audio = r.listen(source)
   text = r.recognize_google(audio)


if "information" in text:
          speak("You need information related to which topic?")

          with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening...")
            audio = r.listen(source)
            infor = r.recognize_google(audio)

            speak("seacrching {} in wikipedia".format(infor))
            print("seacrching {} in wikipedia".format(infor))



            assist = InfoW()
            assist.get_info(infor)


elif "play" and "video" in text:
      speak("you want me to play which video??")

      with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening...")
            video = r.listen(source)
            vid = r.recognize_google(video)
            speak("playing {} on youtube".format(vid))
            print("playing {} on youtube".format(vid))

            assist = Music()
            assist.play(vid)


