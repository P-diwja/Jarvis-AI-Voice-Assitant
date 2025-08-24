Voice Assistant - Jarvis 🎙️🤖

A Python-based voice assistant named Jarvis that listens to your commands and performs actions like opening websites, searching the web, playing YouTube songs, and fetching news.

🚀 Features

🎧 Voice Recognition: Listens to user commands using speech_recognition.

🗣️ Text-to-Speech: Responds using pyttsx3.

🌐 Open Websites: Say open <website> (e.g., "open google").

🔍 Search Queries: Say search <your query> (e.g., "search artificial intelligence").

🎶 Play Songs on YouTube: Say play <song name> (e.g., "play Shape of You").

📑 Quick Info: Ask what is <topic> (e.g., "what is machine learning").

📰 Get Latest News: Just say news.

🛠️ Requirements

Make sure you have Python 3.7+ installed and then install dependencies:

pip install speechrecognition pyttsx3 pywhatkit requests


Also, install PyAudio (required for microphone input):

pip install pyaudio
** all required things that need to be installed are listed in "requirement" file** , go through it...

▶️ How to Run

Clone or download this repository.

Run the script:

python main.py


Say "Jarvis" to activate the assistant.

Give your command (e.g., "open YouTube", "play Believer", "search Python tutorial").

📌 Example Commands

"Jarvis open google" → Opens Google.

"Jarvis play despacito" → Plays the song on YouTube.

"Jarvis search weather today" → Searches Google.

"Jarvis what is AI" → Opens a Google search about AI.

"Jarvis news" → Opens Google News.

⚠️ Notes

Requires a working microphone.

Internet connection is needed for search, news, and YouTube playback.

Can be extended with more commands (e.g., weather API, reminders, etc.).

✨ Future Improvements

Add weather reports via API.

Integrate with email & calendar.

Control system apps (calculator, notepad, etc.).

Smarter natural language processing.
