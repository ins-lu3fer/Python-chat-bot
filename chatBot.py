import random

responses = {
    "hi":["hi","hello","hey","bhai","yarr","yrr"],
    "hello":["hello sir","yes master","ready for command sir","ready master"],
    "hi bro":["haan bhai bol na","bol na yrr","bata","problem kya hai","mat kr bhai mere v family hai"],

#how_are_you = ["bhai kaise ho", "or bhai kya hal", "kaise ho", "how are you", "wassup", "or bhai"]
"how_are_you":["mst bhai,thu bta","arrae ek number yrr","im good","mst","i'm fine","All good!"],

#question = ["bhai thu hai kon?", "who are you", "what is your name", "naam kya hai?", "kya naam hai?", "whats your name"]
"who are you":["Chatbot bolte apun ko","I Am a Bot","Chatbot","i'm Vivek Chatbot"],

#jokes = ["tell me a joke", "joke", "ek mazak ki baat batau", "ek funny joke hai"]
"joke":["I promise I’m not spying on you","math is hard, trust me", "Why do programmers hate nature? Too many bugs 🐛"] ,
"vivek":["He is my master"]
}

while True:
    user = input("You: ").lower()

    if user in responses:
        print("Bot: ",random.choice(responses[user]))

    elif user =="bye":
        print("Bot: Goodson of your father!")    
        break

    else:
        print("Bot: mt kar lala mt kar ")
