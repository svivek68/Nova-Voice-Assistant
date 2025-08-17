import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import urllib.parse
import pywhatkit
import wikipedia



recognizer = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')  # Windows driver

def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    #Opening command
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

        # Play song
    elif "play song" in c.lower():
        speak("Which song should I play?")
        with sr.Microphone() as source:
            print("Listening for song name...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        try:
            song_name = recognizer.recognize_google(audio)
            print("Song name:", song_name)
            pywhatkit.playonyt(song_name)  # Opens YouTube and plays first result

            speak(f"Playing {song_name} on YouTube")
        except:
            speak("Sorry, I could not understand the song name.")

            # Tell me about / Who is
    elif "tell me about" in c.lower() or "who is" in c.lower():
        # Remove trigger words
        query = c.lower().replace("tell me about", "",1).replace("who is", "",1).strip()

        # If multiple names given
        people = [name.strip() for name in query.split("and")]

        for person in people:
            if person:
                try:
                    summary = wikipedia.summary(person, sentences=2)
                    speak(summary)
                except wikipedia.exceptions.DisambiguationError:
                    speak(f"There are multiple results for {person}. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak(f"Sorry, I could not find any information about {person}.")
                except Exception:
                    speak("Something went wrong while searching.")


            
    # Closing commands (Windows example)
    elif "exit google" in c.lower() or "close google" in c.lower():
        os.system("taskkill /im msedge.exe /f")  # Closes Chrome completely
    elif "exit facebook" in c.lower() or "close facebook" in c.lower():
        os.system("taskkill /im msedge.exe /f")
    elif "exit youtube" in c.lower() or "close youtube" in c.lower():
        os.system("taskkill /im msedge.exe /f")
    elif "exit linkedin" in c.lower() or "close linkedin" in c.lower():
        os.system("taskkill /im msedge.exe /f")


if __name__ == "__main__":
    speak("Initializing Nova.....")
    while True:
        r = sr.Recognizer()

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print("Recognized:", word)

            
            if "nova" in word.lower():
                engine.say("Yes Sir")

                with sr.Microphone() as source:
                    print("Nova Active..")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("UnexpectedError:", e)
