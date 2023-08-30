from Body.listen import MicExecution
from Brain.aibrain import ReplyBrain
from Brain.Qna import QuestionsAndAnswers

print(">>Starting The AI Voice Assistant : Wait For Some Seconds.")
from Body.speak import Speak
from Features.clap import Tester
from main import MainTaskExecution

print(">>Starting The AI Voice Assistant : Wait For Few More Seconds.")

def MainExcecution():
    Speak("Hello Sir!!")
    Speak("I'am your AI voice Assistant, How can I help you??")
    while True:
        Data=MicExecution()
        Data=str(Data)

        ValueReturn=MainTaskExecution(Data)
        if ValueReturn==True:
            pass
        elif len(Data)<3:
            pass
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply=QuestionsAndAnswers(Data)
        else:
            Reply=ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():
    query=Tester()
    if "True-Mic" in query:
        print("")
        print(">>Clap Detected!! >>")
        print("")
        MainExcecution()
    else:
        pass
ClapDetect()