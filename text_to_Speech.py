import  pyttsx3  # pip install pyttsx3

# TO text to speech in Python-->
"""
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
"""

"""
    voices = engine.getProperty('voices')  # getting details of current voice
    print(voices)
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    engine.say("I will speak this text")
    engine.runAndWait()
"""
engine = pyttsx3.init()
engine.say("I will speak this text as male")
engine.runAndWait()
voices = engine.getProperty('voices')  # getting details of current voice
print(voices)
engine.setProperty('voice', voices[1].id)
engine.say("I will speak this text as female")
engine.runAndWait()