import random
import os
import pyttsx3

#engine = pyttsx3.init()
#engine.setProperty("rate",170) #we can set speed , voice high or low


# voice function

def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)     # chnge to female

    engine.setProperty('rate',155)      #as i say we can change speed like 200 very fast or 130 very slow...


    engine.say(text)
    engine.runAndWait()
    engine.stop()
    

#Chatbot Response    
responses = {
    "hi":["hi","hello","hey","bhai","yrr"],
    "hello":["hello sir","yes master","ready for command sir","ready master"],
    "hi bro":["haan bhai bol na","bol na yrr","bata","problem kya hai","mat kr bhai mere v family hai"],

#how_are_you = ["bhai kaise ho", "or bhai kya hal", "kaise ho", "how are you", "wassup", "or bhai"]
"how are you":["mst bhai,thu bta","arrae ek number yrr","im good","mst","i'm fine","All good!"],

#question = ["bhai thu hai kon?", "who are you", "what is your name", "naam kya hai?", "kya naam hai?", "whats your name"]
"who are you":["Chatbot bolte apun ko","I Am a Bot","Chatbot","i'm Vivek Chatbot"],

#jokes = ["tell me a joke", "joke", "ek mazak ki baat batau", "ek funny joke hai"]
"joke":["I promise I’m not spying on you","math is hard, trust me", "Why do programmers hate in nature? Too many bugs 🐛","Haha 😂"] ,
"vivek":["He is my master"],
"tanisha":["Vivek loves her 😉"],
"stream":["Opening stream setup"],
"valorant":["Launching Valorant"]
}
  
 # Apps like you want open

apps = {
    "notepad":"notepad.exe",
    "calculator":"calc.exe",
    "paint":"mspaint.exe",
    "cmd":"cmd.exe",
    "valorant":r"D:\game\Riot Games\Riot Client\RiotClientServices.exe"      #r=raw string fix, without r "\" means new line so we use r to no next line ..just keep the string exactly as typed...
}  

#main loops

while True:
    user = input("You: ").lower()

    found = False               #flag usually track somthing like true or false..

#open apps
    for app in apps:
        if app in user:
            os.startfile(apps[app])

            bot_response = "Opening" + app
            print("Bot:  ",bot_response)
            speak(bot_response)

            found = True
            break

#chat responses
    for key in responses:
        if key in user:         #this checks keyword exists inside sentence...
            response = random.choice(responses[key])

            print("Bot: ",response)
            speak(response)

            found = True
            break

    if user =="bye":
        print("Bot: chala ja BSDK!") 
        speak("Chala ja BSDK")   
        break

    if not found and user !="bye":
        print("Bot: mt kar lala mt kar ")
        speak("mat kr lala mt kar")
