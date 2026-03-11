import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
# initialize speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand")
        return ""
# main program
speak("Hello, I am your voice assistant")
while True:
    command = listen()

    if "hello" in command:
        speak("Hello, how can I help you")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today is " + date)

    elif "search" in command or "google" in command:
        speak("What should I search for?")
        query = listen()
        webbrowser.open("https://www.google.com/search?q=" + query)

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break
