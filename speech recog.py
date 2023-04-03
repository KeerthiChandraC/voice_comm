import speech_recognition as sr
import pyttsx3
import requests


def setupVoice():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    return engine

def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.co.in'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        print(urllink.url)

engine = setupVoice()

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():     
    r = sr.Recognizer()     
    with sr.Microphone() as source:         
        print("Listening...")
        r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

if __name__ == '__main__':
    while True:
        speak("Hi, are you a client?")
        query = takeCommand().lower()
        print(query)
        if 'no' in query or 'not' in query:
            speak("What you want to oder?")
            query = takeCommand().lower()
            speak(f'odering {query}')
            googleSearch(query)
        elif 'yes' in query or 'yeah' in query:
            speak("What is your customer Id?")
            query = takeCommand().lower()
            speak(f"hi {query}")
            speak("What you want to oder?")
            query = takeCommand().lower()
            speak(f'odering {query}')
            googleSearch(query)
        else:
            speak("Bad command. Try again")

