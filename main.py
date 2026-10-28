# rule based AI python chatbot
import datetime
import time
name = input("please enter your name;")
timehour = datetime.datetime.now().hour

if 5<= timehour<=11:
    print("\ngood morning", name)
elif 11<= timehour<=17:
    print("\ngood afternoon")
elif 17<= timehour <=20:
    print("\ngoodevening")
else:
    print("\ngood night")

print("\n ===welcome to your chatbot===")

print("\nyou can ask me basic question , and type 'bye' to exit from bot")

#chatbot memory cretion (udsing dictionary)

response = {

    "hello": "Hi, welcom. how can i help you?",
    "how are you": " i am very fine . thank you",
    "who are you": "i am smart AI chatbot",
    "motivate me": "keep going. every bug of your project makes you a better developer ",
    "happy": "great to hear that",
    "happy diwali": "same to you"
}

# method  function to get response of chatbot

def getresponseofbot(userquestion):
    userquestion= userquestion.lower()
    for eachkey in response:
        if eachkey in userquestion:
            return response[eachkey]

    return "i am not able to tell that yet. i learn this soon"

#Take user input

while True:
    userinput = input("please ask your uestion:")


    if "bye" in userinput.lower():
        break

    time.sleep() # wait for 1 second

    reply= getresponseofbot(userinput)
    print(reply)

    
   