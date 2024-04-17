import speech_recognition as sr
from datetime import datetime
import json
import requests

def main():
    while True:
        audio = listen_microphone(recognizer)

        try:
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)
            if "hello alvin" in text:
                print("Hello!")
            elif "bye-bye alvin" in text:
                print("Goodbye!")
                break
            elif "i love you alvin" in text:
                print("<3")    
            elif "alvin what is the bitcoin price" in text:
                get_bitcoin_price()
            elif "alvin what time is it" in text:
                print("Current time is:", datetime.now().strftime("%H:%M:%S"))
            elif "alvin what is the weather" in text:
                get_current_weather()

        except sr.UnknownValueError:
            print("...")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")
def listen_microphone(recognizer):
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=4)
                return audio
            except sr.WaitTimeoutError:
                continue

def get_bitcoin_price():
    api_keys = load_api_keys()
    api_key = api_keys["api_key"]
    api_secret = api_keys["secret_key"]

    endpoint = "https://api.bybit.com/v2/public/tickers"
    params = {"symbol": "BTCUSD"}
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        price = data["result"][0]["last_price"]
        print("Current Bitcoin price:", price)
    else:
        print("Failed to retrieve Bitcoin price. Check your API credentials.")

def load_api_keys():
    with open("api_keys.json", "r") as file:
        api_keys = json.load(file)
    return api_keys

def get_current_weather():
    endpoint = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Pozna%C5%84?unitGroup=metric&key=R7GHTFU8ZTHTXLJFQBWLLF2YK&contentType=json"
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        current_datetime = datetime.now().strftime("%H:00:00")

        current_hour_data = next((hour for hour in data["days"][0]["hours"] if hour["datetime"] == current_datetime), None)

        if current_hour_data:
            current_temp = current_hour_data["temp"]
            current_conditions = current_hour_data["conditions"]
            print(f"Current weather at {current_datetime}: Temperature: {current_temp}°C, Conditions: {current_conditions}")
        else:
            print("Unable to retrieve current weather data.")

    else:
        print("Failed to retrieve weather data. Check the API endpoint and key.")

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    main()
