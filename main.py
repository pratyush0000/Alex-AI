import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()




def start():
    command = ""  # Add a default value for the command
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alex" in command:
                command = command.replace('alex ', '')
    except sr.UnknownValueError:
        # If the speech cannot be recognized, print an error message
        print("Sorry, I could not understand your speech.")
    except sr.RequestError:
        # If there is an issue with the API or the internet connection, print an error message
        print("Sorry, there was an error connecting to the speech recognition service.")
    return command

def rerun():
    print("do you need help with anything else? Yes or No")
    talk("do you need help with anything else? Yes or No")
    with sr.Microphone() as source:
        print("listening...")
        sound = listener.listen(source)
        reply = listener.recognize_google(sound)
        reply = reply.lower()
        if 'yes' in reply:
            print("Okay. How may I help you?")
            talk("Okay. How may I help you?")
            runalex()
        elif 'no' in reply:
            print("Ok thank you. Bye.")
            talk("OK thank you. Bye.")
            exit()
        else:
            talk("please repeat")
            rerun()


def runalex():
    command = start()
    if 'play' in command:
        song = command.replace("play","")
        print("playing" + song)
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("The time right now is " + time)
    elif 'tell me about' in command:
        wik = command.replace('tell me about','')
        info = wikipedia.summary(wik,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        print("Sorry, I did not get you")
        talk("sorry i did not get you")
    rerun()



print("I am Alex A.I. How may I help you today?")
talk("I am Alex A.I. How may I help you today?")
runalex()