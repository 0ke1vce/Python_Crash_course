import os
import win32com.client as wincom

if __name__ == '__main__':
    speak = wincom.Dispatch("SAPI.SpVoice")
    print("Welcome to Robo speaker. Created by Ujjwal")
    while True:
            x=input("Enter what you want to speak\nEnter q to exit the program\n")
            command = speak.Speak(x)
            os.system(str(command))
            if (x == "q"):
                os.system(speak.Speak("By by friends"))
                break



