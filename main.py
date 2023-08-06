import datetime
import re

import speech_recognition as sr
import pyttsx3 as tts
import wikipedia as wikki

listener = sr.Recognizer()
engine = tts.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(str):
    engine.say(str)
    engine.runAndWait()

alexa_list = ['hi alexa','hey alexa']

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice = listener.listen(source,3)
            print(voice)
            command = listener.recognize_google(voice)
            print(command)
            command = command.lower()
            print(command)
            if 'alexa' in command:
                regex = re.compile('|'.join(map(re.escape, alexa_list)))
                command = regex.sub('', command)
                print(command)
                return command
    except Exception as ex:
        print(ex)

wikki_list = ['who is', 'tell me about']


def run_alexa():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I : %M %p")
        talk(time)
    elif any(ele in command for ele in wikki_list):
        regex = re.compile('|'.join(map(re.escape,wikki_list)))
        actualData = regex.sub('',command)
        print('actualdata is',actualData)
        data = wikki.summary(actualData,1)
        talk(data)
    else:
        talk("Please try again")


while True:
    run_alexa()
