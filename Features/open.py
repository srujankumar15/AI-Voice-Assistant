import os
import webbrowser
from time import sleep

import keyboard
import pyautogui


def OpenExe(Query):
    Query=str(Query).lower()

    if "visit" in Query:
        NameOfWeb=Query.replace("visit","")
        Link=f"https://www.{NameOfWeb}.com"
        webbrowser.open(Link)

    elif "launch" in Query:
        NameOfWeb=Query.replace("launch","")
        Link=f"https://www.{NameOfWeb}.com"
        webbrowser.open(Link)

    elif "open" in Query:
        NameOfApp=Query.replace("open","")
        pyautogui.press("win")
        sleep(1)
        keyboard.write(NameOfApp)
        sleep(1)
        keyboard.press("enter")
        sleep(0.5)
        return True

    elif "start"  in Query:
        NameOfApp=Query.replace("open","")
        pyautogui.press("win")
        sleep(1)
        keyboard.write(NameOfApp)
        sleep(1)
        keyboard.press("enter")
        sleep(0.5)
        return True

#OpenExe("open chrome")

