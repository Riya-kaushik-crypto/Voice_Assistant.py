import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.say("Namaste ,  Aman sir I am your Assistant, how are you today may i help you  ?")
engine.runAndWait()
import datetime
import wikipedia
import webbrowser
import os
import sys
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, I'm having trouble with the speech service.")
        return None
def handle_command(command):
    if 'hello' in command:
        speak("Hello Riya Mam, I am your Health care Assistant . How are you feeling today")
    elif 'alexa' in command:
        speak("she is my COMPITITOR")   
    elif 'thank You' in command:
        speak("its my pleasure sir dont be emotional")        
    elif 'time' in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")  
    elif 'date' in command:
        today = datetime.date.today()
        speak(f"Today's date is {today}")   
    elif 'wikipedia' in command:
        speak("What do you want to know from Wikipedia?")
        query = listen()
        if query:
            speak(f"Searching Wikipedia for {query}")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results, please be more specific.")
            except wikipedia.exceptions.HTTPTimeoutError:
                speak("Wikipedia search timed out. Please try again later.")    
    elif 'open' in command:
        search_query = command.split("open")[-1].strip()
        if "google" in search_query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
        elif "youtube" in search_query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")
        else:
            speak("I can only open Google and YouTube for now.")    
    elif 'play music' in command:
        speak("Playing music for you.")      
        os.system("start music.mp3")  
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye!")
        sys.exit()
def main():
    speak("")   
    while True:
        command = listen()
        if command:
            handle_command(command)
if __name__ == "__main__":
    main()
 