import speech_recognition as sr 
import pygame
import datetime
import webbrowser
import pywhatkit as kit
import random as rd
import pyttsx3
import wikipedia
import pyjokes
import requests
import FaceMode  # For switching to face detection

# OpenWeatherMap API Key
API_KEY = "80590db90b5686dc7b68057edb05d6ec"

# Fun facts & quotes
fun_facts = [
    "Bananas are berries, but strawberries are not.",
    "Honey never spoils. Archaeologists have found edible honey in ancient tombs.",
    "Octopuses have three hearts.",
    "Sharks existed before trees.",
    "A day on Venus is longer than a year on Venus."
]

quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don't let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Do something today that your future self will thank you for."
]

wikipedia.set_lang("en")
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("..", end=" ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("..", end=" ")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        print("Sorry, I didn't catch that.")
        return "None"
    return query.lower()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you today?")

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            speak(f"The current temperature in {city} is {temp} degrees Celsius with {desc}.")
        else:
            speak("I couldn't find weather information for that location.")
    except Exception:
        speak("Sorry, I couldn't retrieve the weather at the moment.")

def bramii():
    wish_user()
    pygame.mixer.init()
    is_music_playing = False
    volume = 0.5
    pygame.mixer.music.set_volume(volume)

    while True:
        query = take_command()

        # Mode switching
        if "switch to face detection" in query:
            speak("Switching to Face Detection Mode.")
            FaceMode.face()
            continue
        elif "switch to chat mode" in query:
            speak("Switching back to Chat Mode.")
            break

        if 'time' in query:
            speak(f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}")

        elif 'youtube' in query:
            q = query.replace('open', "").replace('search', "").replace('youtube', "").replace('play', "").replace('and', "").strip()
            if not q:
                speak("What should I play on YouTube?")
                q = take_command()
            if q and q != "None":
                speak(f"Playing {q} on YouTube")
                kit.playonyt(q)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            try:
                x = rd.randint(2, 5)
                result = wikipedia.summary(query, sentences=x)
                speak("According to Wikipedia")
                speak(result)
            except wikipedia.DisambiguationError:
                speak(f"The topic '{query}' is too ambiguous.")
            except wikipedia.PageError:
                speak("Page not found.")
            except Exception:
                speak("Error searching Wikipedia.")

        elif 'play online' in query or 'online song' in query:
            song_name = query.replace("play online", "").replace("online song", "").strip()
            file_path = download_and_play_youtube_audio(song_name, music_dir)  # Must be defined elsewhere
            if file_path:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                is_music_playing = True

        elif 'pause' in query and is_music_playing:
            pygame.mixer.music.pause()
            speak("Music paused.")

        elif 'resume' in query and is_music_playing:
            pygame.mixer.music.unpause()
            speak("Resuming music.")

        elif 'volume up' in query or 'increase volume' in query:
            if volume < 1.0:
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)
                speak(f"Volume increased to {int(volume * 100)} percent.")
            else:
                speak("Volume is already at maximum.")

        elif 'volume down' in query or 'decrease volume' in query:
            if volume > 0.0:
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)
                speak(f"Volume decreased to {int(volume * 100)} percent.")
            else:
                speak("Volume is already at minimum.")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'fun fact' in query:
            fact = random.choice(fun_facts)
            speak(fact)

        elif 'quote' in query:
            quote = random.choice(quotes)
            speak(quote)

        elif 'weather' in query:
            city = query.replace("weather in", "").replace("what's the weather in", "").strip()
            if city:
                get_weather(city)
            else:
                speak("Please tell me the city name.")

        elif 'open portfolio' in query:
            speak("Opening portfolio...")
            webbrowser.open("https://bramhendra-protofolio.netlify.app/")

        elif 'search' in query or 'google' in query:
            q = query.replace("search", "").replace("google", "").strip()
            speak(f"Searching Google for {q}")
            webbrowser.open(f"https://www.google.com/search?q={q}")

        elif 'exit' in query or 'stop' in query or 'bye' in query or 'exit from bramii mode' in query:
            speak("Exiting Bramii mode.")
            break
