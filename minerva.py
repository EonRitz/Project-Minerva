import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import os
#import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes # pip install pyjokes

# Defining the Voice Engine used

engine = pyttsx3.init()
voices = engine.getProperty('voices')
desired_voice = voices[3]
engine.setProperty('voice', desired_voice.id)

# Functions of Minerva AI Assistant

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak(f"The current time is {Time}")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = months_list[(month - 1)]
    day = int(datetime.datetime.now().day)
    speak(f"Today is {month} {day} in the year {year}.")

def greetings():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        hour_of_day = "morning"
    elif hour >=12 and hour <18:
        hour_of_day = "afternoon"
    elif hour >=18 and hour <24:
        hour_of_day = "evening"
    else:
        hour_of_day = "night"
    speak(f"Good {hour_of_day}... It's a pleasure to have you here.")
    date()
    time()
    speak("Welcome! I am Minerva, your intelligent virtual assistant! How can I assist you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I am listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Please say the again")
        return "None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xyza@gamil.com', 'Password')
    server.sendmail('r.chichirita@gmail.com', to, content)
    server.close()

# def screenshot():
    # img = pyautogui.screenshot()
    # img.save("screenshot\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak(f'CPU is at {usage} percentage')
    battery = psutil.sensors_battery()
    speak(f'and the Battery is at {battery.percent} percent.')

def jokes():
    speak(pyjokes.get_joke())

def weather():
    import requests
    from bs4 import BeautifulSoup

    speak("Which city, do you want to know the weather of?")
    city = takeCommand()

    url = f'https://wttr.in/{city.replace(" ", "+")}?format=%C+%t+%w'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        weather_info = soup.get_text()
        print(f"Weather in {city}: {weather_info}")
        speak(f"Weather in {city}: {weather_info}")
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        speak(f"Failed to fetch weather data. Status code: {response.status_code}")


# Main body of Minerva AI Assistant

if __name__ == "__main__":
    greetings()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak("According to Wikipedia...")
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'roner@hotmail.ph'
                # sendmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to end the email")

        elif 'open in chrome' in query:
            speak("What should I search for?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'music/'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said, to remeber that..." + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said, to remember that..." + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot taken!")
        
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'weather' in query:
            weather()

        elif 'offline' in query:
            quit()