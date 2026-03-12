import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes
import time

# initialize speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)


def greet():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning")
    elif hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am your voice assistant. How can I help you?")


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=5)

    try:
        command = r.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command

    except:
        print("Could not understand")
        return ""


greet()

while True:

    command = listen()

    if command == "":
        continue

    if "hello" in command:
        speak("Hello, how can I help you")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + current_time)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today is " + today)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query != "":
            webbrowser.open("https://www.google.com/search?q=" + query)

    elif "who is" in command or "what is" in command:
        try:
            result = wikipedia.summary(command, sentences=2)
            speak(result)
        except:
            speak("Sorry, I could not find information")

    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "play music" in command:
        speak("Playing music")
        webbrowser.open("https://www.youtube.com")

    elif "stop" in command or "exit" in command or "bye" in command:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I did not understand that command")
