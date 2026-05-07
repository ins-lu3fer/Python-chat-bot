import pyttsx3


import os

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