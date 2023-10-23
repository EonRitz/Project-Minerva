import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
desired_voice = voices[3]
engine.setProperty('voice', desired_voice.id)


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

def wishme():
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
        r.pause_threshold = 1.5
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
    server.login('r.chichirita@gamil.com', 'Remuneration')
    server.sendmail('r.chichirita@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
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
                sendmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to end the email")

        elif 'offline' in query:
            quit()