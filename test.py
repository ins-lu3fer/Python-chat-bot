import pyttsx3



import os
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")

    r.energy_threshold = 300
    r.pause_threshold = 1

    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)

except Exception as e:
    print(e)
engine = pyttsx3.init()

engine.say("Hello sir")
engine.runAndWait()
#greetings=["Hi","Hello","Hey"]
#import random
#greetings=["Hi","Hello","Hey"]
#user = input("You:  ").lower()

#if user in ["hi","hello","hey"] :
#print(random.choice(greetings))
#def greet():
  #  print("Hello!")

#greet()
#def reply(user):
  #  print("you said : ",user)

#
# reply("hello")   
user = input("you: ").lower()
if "notepad" in user: 
      os.startfile("notepad.exe")