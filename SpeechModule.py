#!./venv/bin/python
import speech_recognition as sr
import time
from datetime import datetime
# source venv/bin/activate

def listen_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    return audio

def main():
    while True:
        audio = listen_microphone()

        try:
            # Use the Google Web Speech API to convert speech to text
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)

            if "tedy" in text:
                handle_command(text)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")

def handle_command(text):
    if "what time is it" in text:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current time is:", current_time)

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    main()


import speech_recognition as sr
import time
from datetime import datetime

def listen_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    return audio

def main():
    while True:
        audio = listen_microphone()

        try:
            # Use the Google Web Speech API to convert speech to text
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)

            if "tedy" in text:
                handle_command(text)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")

def handle_command(text):
    if "what time is it" in text:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current time is:", current_time)

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    main()
