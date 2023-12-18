#!./venv/bin/python
# project_env\Scripts\activate.bat
import speech_recognition as sr
from datetime import datetime
import json
import requests

def listen_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=4)

    return audio

def main():
    recognizer = sr.Recognizer()
    api_keys = load_api_keys()
    api_key = api_keys["api_key"]
    api_secret = api_keys["secret_key"]

    while True:
        audio = listen_microphone()

        try:
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)
            if "hello alvin" in text:
                print("Hello!")
            elif "bye-bye alvin" in text:
                print("Goodbye!")
            elif "alvin what is the bitcoin price" in text:
                get_bitcoin_price()
            # elif "alvin what is my crypto wallet balance" in text:
                # get_bybit_balance(api_key, api_secret)
            elif "alvin what time is it" in text:
                print("Current time is:", datetime.now().strftime("%H:%M:%S"))

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")

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

def get_bybit_balance(api_key, api_secret):
    endpoint = "https://api.bybit.com/v2/private/wallet/balance"

    # Generate the required headers, including timestamp and API signature
    headers = generate_bybit_headers(api_key, api_secret)

    try:
        # Make the API request
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        print("API Response:", data)  # Print the entire response

        # Modify the following line based on the actual structure of the JSON response
        balance = data["result"]["equity"]
        print("Your Bybit balance is:", balance)

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
    except KeyError as e:
        print(f"Error accessing wallet balance: {e}")

def generate_bybit_headers(api_key, api_secret):
    import hashlib
    import hmac
    import time

    # Generate a timestamp and prepare the request path
    timestamp = str(int(time.time() * 1000))
    path = "/v2/private/wallet/balance"

    # Concatenate the components to create the string to sign
    sign_string = f"{path}{timestamp}"
    
    # Generate the API signature using HMAC-SHA256
    signature = hmac.new(api_secret.encode(), sign_string.encode(), hashlib.sha256).hexdigest()

    # Construct the headers
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
        "timestamp": timestamp,
        "sign": signature,
    }

    return headers
    endpoint = "https://api.bybit.com/v2/private/wallet/balance"

    # Set your API keys
    headers = {
        "Content-Type": "application/json",
        "api_key": api_key,
        "api_secret": api_secret,
    }

    try:
        # Make the API request
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        print("API Response:", data)  # Print the entire response

        # Modify the following line based on the actual structure of the JSON response
        balance = data["result"]["equity"]
        print("Your Bybit balance is:", balance)

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
    except KeyError as e:
        print(f"Error accessing wallet balance: {e}")

def load_api_keys():
    with open("api_keys.json", "r") as file:
        api_keys = json.load(file)
    return api_keys

if __name__ == "__main__":
    main()
