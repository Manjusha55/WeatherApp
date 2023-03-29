import win32com.client as wincom
import requests
import json

city = input("Enter name of the city ")
url = f'https://api.weatherapi.com/v1/current.json?key=a424df3def0f4252be3101257232803&q={city}'

r = requests.get(url)
# print(r.text)
speak = wincom.Dispatch("SAPI.SpVoice")
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(w)
speak.Speak(f'The current Weather in {city} is {w} degree')