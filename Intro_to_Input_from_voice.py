import speech_recognition as s_r
import pyaudio
import pyttsx3

# Object created for taking output from speaker.
engine = pyttsx3.init()

# Speech recognition (microphone--> input)
"""
Set microphone to accept sound
my_mic = s_r.Microphone()

To recognize input from the microphone you have to use a recognizer class. Let’s just create one.
r = s_r.Recognizer()

Now we have to capture audio from microphone. To do that we can use the below code:
with my_mic as source:
    print("Say now!!!!")
    audio = r.listen(source)

Convert the sound or speech into text in Python
To convert using Google speech recognition we can use the following line:
r.recognize_google(audio)
It will return a string with some texts. ( It will convert your voice to texts and return that as a string.

You can simply print it using the below line:
print(r.recognize_google(audio))


Now you have to reduce noise from your input.
How to do that?
 r.adjust_for_ambient_noise(source)

# r.recognize_google(audio) this will return string.
"""

print(s_r.__version__) # just to print the version not required
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone
x=r.recognize_google(audio) #to print voice into text

# to get our inputed voice from speaker
print("you say ")
engine.say(x)
engine.runAndWait()
