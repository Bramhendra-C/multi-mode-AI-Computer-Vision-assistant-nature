import wikipedia
import pyttsx3
import random as rd
import sys
import os
try:
    import BramiiMode  # Updated Bramii mode file
    import FaceMode    # Face detection mode file
except ImportError as e:
    print(f"Error: Missing module - {e}")
    sys.exit(1)

# Initialize TTS
wikipedia.set_lang("en")
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wikipedia_search(query):
    """Search Wikipedia and show top 5 Google links."""
    print('Searching Wikipedia...')
    query = query.replace("wikipedia", "").strip()
    try:
        sentences_count = rd.randint(2, 5)
        result = wikipedia.summary(query, sentences=sentences_count)
        print("\nAccording to Wikipedia:\n", result)
    except wikipedia.DisambiguationError:
        print(f"The topic '{query}' is too ambiguous.")
    except wikipedia.PageError:
        print("Page not found.")
    except Exception:
        print("Error searching Wikipedia.")

def show_menu():
    """Display mode selection menu."""
    print("\n========== Voice & Face Assistant ==========")
    print("1. Chatbot Mode (Text)")
    print("2. Bramii Mode (Voice Assistant)")
    print("3. Face Detection Mode")
    print("4. Exit")
    print("============================================")

def main():
    speak("Welcome! I am your assistant.")
    while True:
        show_menu()
        choice = input("Select mode (1/2/3/4): ").strip()

        if choice == "1":
            speak("Entering Chatbot Mode")
            while True:
                query = input("\nEnter your query ('back' to return to menu): ").lower().strip()
                if query in ["back", "exit", "quit"]:
                    speak("Returning to main menu.")
                    break
                elif "wikipedia" in query:
                    wikipedia_search(query)
                else:
                    wikipedia_search(query)  # Default to Wikipedia search

        elif choice == "2":
            speak("Switching to Bramii Mode.")
            BramiiMode.bramii()

        elif choice == "3":
            speak("Switching to Face Detection Mode.")
            FaceMode.face()

        elif choice == "4":
            speak("Goodbye! Have a great day.")
            sys.exit(0)
            os.system('cls')

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Exiting program. Goodbye!")
        sys.exit(0)
        cv2.destroyAllWindows()