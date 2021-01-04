import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        audio = r.listen(source)

    try:
        print('Recognizing')
        speak("jarvis searching")
        queryy = r.recognize_google(audio, language='en-in')
        print(f"user said: {queryy}\n")

    except Exception as e:
        print('Say that again')
        queryy = None
    return queryy

while(True): # for making assistant continuously listen us
    speak("Hi! i'm pari's assistant how can i help you?")
    query = takecommand()

    if query == None: # If not properly heard, assistant will again listen
        continue
    
    elif 'thank you' in query.lower(): # To end the assistant, say 'Thank you'
        speak("Thank you for giving me chance to serve you Pari")
        break

    elif 'wikipedia' in query.lower():
        speak('searching wikipedia..')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(results)


    elif 'open youtube' in query.lower():
        url = 'https://www.youtube.com'
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open(url)


    elif 'open google' in query.lower():
        url = 'https://www.google.com'
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open(url)


    elif 'open whatsapp' in query.lower():
        url = 'https://web.whatsapp.com'
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open(url)


    elif 'open instagram' in query.lower():
        url = 'https://www.instagram.com'
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open(url)


    elif 'open google meet' in query.lower():
        url = 'https://meet.google.com'
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open(url)


    elif 'open facebook' in query.lower():
        url = 'https://www.facebook.com'
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open(url)


    elif 'open video' in query.lower():
        songs_dir = "E:\\video"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))


    elif "write down" in query:
        speak("what shall i write for you P?")
        note = takecommand()
        remember = open("data.txt", 'w')
        remember.write(note)
        remember.close()
        speak("I know you never remember anything")
        speak("I have noted that" + note)


    elif "reminder" in query:
        remember = open("data.txt", 'r').read()
        speak("you asked me to remind you that" + remember)
