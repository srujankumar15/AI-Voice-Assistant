import pyaudio
import speech_recognition as sr
from googletrans import Translator


def Listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source,0,8)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en")
    except:
        return ""
    query=str(query).lower()
    return query
#print(Listen())

def TranslateToEnglish(Text):
    line=str(Text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    print(f"You : {data}.")
    return data

#TranslateToEnglish("कैसे हो भाई साहब")

def MicExecution():
    query=Listen()
    data=TranslateToEnglish(query)
    return data
