import requests
import os
import datetime as dt

def my_weather_app():

    print(f"Current working directory:{os.getcwd()}")

    try:
        with open('E:/Dishant_DE_Study/MK_Python/Python_practice/concepts/DA_Weather_App/da_weather_api.txt',"r") as f:
            API_KEY =f.read().strip() 
            print("API Key being used:", repr(API_KEY))  # Debug: shows hidden characters
    except Exception as e:
        # print("The error is:",e)
        raise e
    CITY = "London"

    COMP_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric" 

    
    response = requests.get(COMP_URL)
    data=response.json()
    # print(data)
    if data['cod'] ==200:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
    else :
        print(f"City not found. Please check again.")

my_weather_app()


# Read API key safely
# with open("da_weather_api.txt", "r", encoding="utf-8") as f:
#     API_KEY = f.read().strip()

# print("API Key being used:", repr(API_KEY))  # Debug: shows hidden characters

# city = "Gurugram"
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# response = requests.get(url)
# print(response.json())
