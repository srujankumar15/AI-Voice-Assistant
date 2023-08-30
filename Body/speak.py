import pyttsx3


def Speak(text):
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    print("")
    print(f"AI : {text}.")
    print("")
    engine.say(text)
    engine.runAndWait()

#Speak("How are You")