import requests
import json
import  os
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
city=input("Enter the name of the city ")
url=f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r=requests.get(url)
# print(r.text)
dic=json.loads(r.text)
w=dic["current"]["temp_c"]
os.system(speak.Speak(f"The current temprature in {city} is {w} degree"))
