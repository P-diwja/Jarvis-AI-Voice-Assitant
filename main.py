import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
import requests
# from bs4 import BeautifulSoup

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

  

def processCommand(word):
    if "open" in word.lower():
        # Extract the website name from the word
        website = word.lower().replace("open", "").strip()
        url = f"https://{website}.com"
        webbrowser.open(url)
        speak(f"Opening {website}")
    elif "search" in word.lower():
        # Extract the search query from the word
         query = word.lower().replace("search", "").strip()
         url = f"https://www.google.com/search?q={query}"
         webbrowser.open(url)
         speak(f"Searching for {query}")

    elif "play" in word.lower():
        # Extract the song name from the word
        # song = word.lower().replace("play", "").strip()
        # url = f"https://www.youtube.com/results?search_query={song}"
        # webbrowser.open(url)
        # speak(f"Playing {song} on YouTube")
       
        song = word.replace('play', '').strip()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
        
  
    elif "what is" in word.lower():
        # Extract the query from the word
        query = word.lower().replace("what is", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching for {query}")
  
    elif "news" in word.lower():
        # Open the news website
        url = "https://news.google.com"
        webbrowser.open(url)
        speak("Opening news website")
  
    else:
        speak("Sorry, I didn't understand that command. Please try again.") 
                             


if __name__ == "__main__":
    speak(" hey diwja, Initializing jarvis....")
    while True:
        # listen for wake up word
        r = sr.Recognizer()
       
        
        try:
          with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2,phrase_time_limit=5)
            # print("Recognizing...") 
           # recognize speech using Google Speech Recognition
            word = r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("Yyyupppp,how can I help you?")

                speak("jarvis is listening...")

                audio = r.listen(source)
                word = r.recognize_google(audio)
                
                processCommand(word)
                # Here you can add more commands to process

            print(word)

        except Exception as e:
            print("Could not understand the audio")
            continue    
             

        

    