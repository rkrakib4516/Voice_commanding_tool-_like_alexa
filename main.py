import pywhatkit
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pwt
import datetime
import wikipedia
import pyjokes



listener=sr.Recognizer()
Alexa = pt.init()
voices = Alexa.getProperty('voices')
Alexa.setProperty('voice', voices[1].id)
def talk(text):
    Alexa.say(text)
    Alexa.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice=listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Alexa' in command:
                print(command)

    except:
        pass
    return command

def run_alexa():
    command= take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pwt.playonyt(song)
    elif 'tell me about' in command:
        read= command.replace('tell me about','')
        info = wikipedia.summary(read,1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
    elif 'love' in command:
        talk('I am sorry brother already I have a boyfriend')
    else:
        talk('I did not understand but i am going to search for you in google')
        pywhatkit.search(command)
while True:
    run_alexa()
