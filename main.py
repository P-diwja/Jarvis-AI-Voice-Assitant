# Importing required libraries
import speech_recognition as sr    # For speech-to-text conversion
import webbrowser                  # For opening websites in the default browser
import pyttsx3                     # For text-to-speech conversion
import pywhatkit                   # For playing YouTube videos, sending WhatsApp messages, etc.
import requests                    # For making HTTP requests (not used here, but can be used for APIs)
# from bs4 import BeautifulSoup    # (commented out) Can be used for web scraping if needed

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out text using pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process user commands
def processCommand(word):
    if "open" in word.lower():
        # Open a specific website
        website = word.lower().replace("open", "").strip()  # Extract website name
        url = f"https://{website}.com"                      # Construct URL
        webbrowser.open(url)
        speak(f"Opening {website}")

    elif "search" in word.lower():
        # Perform a Google search
        query = word.lower().replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching for {query}")

    elif "play" in word.lower():
        # Play a song/video on YouTube
        song = word.replace('play', '').strip()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)  # Opens YouTube and plays the song

    elif "what is" in word.lower():
        # Search a definition or general query
        query = word.lower().replace("what is", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching for {query}")

    elif "news" in word.lower():
        # Open Google News
        url = "https://news.google.com"
        webbrowser.open(url)
        speak("Opening news website")

    else:
        # Default response for unknown commands
        speak("Sorry, I didn't understand that command. Please try again.") 


# Main program execution
if __name__ == "__main__":
    speak("Heyyy, Initializing Jarvis....")

    while True:
        # Reinitialize recognizer each time to avoid errors
        r = sr.Recognizer()
       
        try:
            # Use the microphone as input source
            with sr.Microphone() as source:
                print("Listening...")
                # Listen for audio (2s timeout, 5s max phrase length)
                audio = r.listen(source, timeout=2, phrase_time_limit=5)

                # Convert speech to text using Google API
                word = r.recognize_google(audio)

                # Check if wake word ("jarvis") is spoken
                if(word.lower() == "jarvis"):
                    speak("Yyyupppp, how can I help you?")
                    speak("Jarvis is listening...")

                    # Listen for the actual command after wake word
                    audio = r.listen(source)
                    word = r.recognize_google(audio)

                    # Process the given command
                    processCommand(word)

                # Print recognized word for debugging
                print(word)

        except Exception as e:
            # If speech not recognized, print error and continue
            print("Could not understand the audio")
            continue
