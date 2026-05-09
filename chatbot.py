import random
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

def take_command():
    r = sr.Recognizer()   #sr=short form of speech recognize
    try:
        with sr.Microphone() as source:   #sr=source=microphone
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            r.pause_threshold = 1.2        #not end sentence to early 
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            
        command = r.recognize_google(audio)     # # convert text into audio by this send audio to google recognizer
        print("You:", command)
        return command.lower()
    except sr.WaitTimeoutError:
        print("No speech detected")
        return ""
    except sr.UnknownValueError:      #voice cant understand by google
        print("Could not understand audio")
        return ""
    except sr.RequestError:        #no internet
        print("Internet issue")
        return ""                       #return empty string bcz of loop continue


def speak(text):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)   # female voice
        else:
            engine.setProperty('voice', voices[0].id)   # fallback if only 1 voice
        engine.setProperty('rate', 145)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"Voice error: {e}")

 #chatbot responses
responses = {
    "hi": ["hi", "hello", "hey"],
    "hello": ["hello sir", "yes master", "ready for command sir", "ready master"],
    "how are you": ["mst bhai thu bta", "im good", "mst", "i'm fine", "All good!"],
    "who are you": ["Chatbot bolte apun ko", "I Am a Bot", "i'm Vivek Chatbot"],
    "joke": ["I promise I'm not spying on you", "math is hard, trust me", "Why do programmers hate nature? Too many bugs"],
    "vivek": ["He is my master"],
    "tanisha": ["Vivek loves her"],
    "stream": ["Opening OBS for you master"],
    "valorant":["Opening valorant sir"]
}

#app u want to open
apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "valorant": r"D:\game\Riot Games\Riot Client\RiotClientServices.exe",
    "stream" :r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"
}
 
 #website to search
websites = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com/ins-lu3fer"
}


#  MAIN LOOP 
while True:
    user = take_command()

    if not user:
        continue                    # skip empty input

    found = False          #flag=found somthing to check like true or false

    # 1. Bye check
    if "bye" in user:
        print("Bot: Phali fursat se nikal!")
        speak("Have a Goodday!")
        break

    # 2. Open websites
    for site in websites:
        if site in user:
            webbrowser.open(websites[site])
            print("Bot: Opening", site)
            speak("Opening " + site)
            found = True
            break

    # 3. Search Google
    if not found and "search" in user:
        query = user.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        print("Bot: Searching", query)
        speak("Searching " + query)
        found = True

    # 4. Open apps
    if not found:
        for app in apps:
            if app in user:
                os.startfile(apps[app])
                print("Bot: Opening", app)
                speak("Opening " + app)
                found = True
                break

    # 5. Chat responses
    if not found:
        for key in responses:
            if key in user:
                response = random.choice(responses[key])
                print("Bot:", response)
                speak(response)
                found = True
                break
    #6. time
    if "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M %p")

        print("Bot:", current_time)
        speak(f"The time is{current_time}")

        found=True   

    # 7.date
    if "date" in user:
        today = datetime.datetime.now().strftime("%d %B %Y")
        print("Bot:", today)
        speak(f"Today's date is {today}")

        found = True   

    
    # 8.day
    elif"What day" in user or "day today" in user:
        day = datetime.datetime.now().strftime("%A")

        print("Bot",day)
        speak(f"Today is {day}")

        found = True 


    # 9.whether
    elif"weather" in user:
        webbrowser.open("https://www.google.com/search?q=weather")

        print("Bot: Opening weather")
        speak("Opening weather")

        found = True    

    
    
    # 10. No match
    if not found:
        print("Bot: mt kar lala mt kar")
        speak("I dont understand")
