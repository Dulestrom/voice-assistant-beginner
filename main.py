import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pywhatkit
import os
import wikipedia

#Function that listens to our mic and returns audio as text using Google

def transform():
    r = sr.Recognizer() #recognizes speech
    with sr.Microphone() as source: #use mic as source
        r.pause_threshold = 0.8 #just a pause threshold
        said = r.listen(source) #we listen to the source
        try:
            print("I am listening....")
            q = r.recognize_google(said, language="en") #calls to Google to recognize the specified language
            return q
        except sr.UnknownValueError: #catches an error if the value returned is unknown
            print("Sorry I didn't catch that.")
            return "I am listening...."
        except sr.RequestError: #catches an error if the service is unavailable
            print("Sorry the service is down.") 
            return "I am waiting...."
        except: #random error we didn't expect
            return "I am waiting...."

def speak(message):
    engine = pyttsx3.init() #initializes the tts
    engine.say(message) #gives the tts what to say
    engine.runAndWait() #runs

# How to change the voice of the assistant :)

#engine = pyttsx3.init()
#for voice in engine.getProperty('voices'):
    #print(voice)
#id = link\to\voices
#engine.setProperty('voice', id)
#engine.say('Hello, World!')
#engine.runAndWait()

#Returns the weekday name

def query_day():
    current_day = datetime.date.today()
    current_weekday = current_day.weekday()
    mapping = {
        0 : 'Monday',
        1 : 'Tuesday',
        2 : 'Wednesday',
        3 : 'Thursday', 
        4 : 'Friday',
        5 : 'Saturday',
        6 : 'Sunday'
    }
    try:
        speak(f'Today is {mapping[current_weekday]}')
    except:
        pass

#Returns the date

def query_date():
    current_date = datetime.date.today()

    month_map = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December"
    }

    speak(f'Today is the {current_date.day} of {month_map[current_date.month]}')

#Returns the year

def query_year():
    current_year = datetime.date.today()
    speak(f'It\'s the year {current_year.year}')

#Returns the time

def query_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f'It is {current_time[0]}{current_time[1]} o\'clock and {current_time[3]}{current_time[4]} minutes.')

#Introduction from our VA

def greetings():
    speak('''Hello! My name is DVA.
    How can I assist you today?''')

#Core

def core(): 
    greetings()
    start = True
    while(start):
        q = transform().lower()

        if 'hello' in q or 'hi' in q or 'hey' in q:
            speak('Hi!')
            continue

        elif 'start youtube' in q or 'open youtube' in q:
            speak("Firing up YouTube!")
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'start browser' in q or 'open browser' in q:
            speak("Opening your default browser!")
            webbrowser.open('https://www.google.com')
            continue

        elif 'what time is it' in q or 'what\'s the time' in q:
            query_time()
            continue

        elif 'what day is it' in q:
            query_day()
            continue

        elif 'what date is it' in q or 'what\'s today\'s date' in q:
            query_date()
            continue

        elif 'what year is it' in q:
            query_year()
            continue

        elif 'search wikipedia for' in q:
            speak('Checking Wiki.')
            q = q.replace("search wikipedia for", "")
            wiki_result = wikipedia.summary(q, sentences=2) #sentences limits how many sentences the query returns
            speak("This is what I found on Wikipedia:")
            speak(wiki_result)
            continue

        elif 'your name' in q:
            speak("My name is DVA, short for D's Voice Assistant.")
            continue

        elif 'thank you' in q or 'thanks' in q:
            speak("You're welcome!")
            continue

        elif 'search web for' in q:
            q = q.replace('search web for', "")
            pywhatkit.search(q)
            speak("This is what I found.")
            continue

        elif 'play' in q:
            q = q.replace('play', "")
            speak(f'Playing {q} on YouTube.')
            pywhatkit.playonyt(q)
            continue

        elif 'joke' in q:
            speak(pyjokes.get_joke())
            continue

        elif 'awesome' in q:
            speak("I know I'm awesome! I was made by an awesome dude!")
            continue

        elif 'goodbye' in q:
            speak("Goodbye!")
            break

core()
