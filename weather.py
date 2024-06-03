import tkinter as tk
import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        weather_info = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            # Add more weather data fields as needed
        }
        update_display(weather_info)
    else:
        weather_label.config(text="City not found")

def update_display(weather_info):
    temperature_label.config(text=f"Temperature: {weather_info['temperature']}°C")
    description_label.config(text=f"Description: {weather_info['description']}")
    wind_speed_label.config(text=f"Wind Speed: {weather_info['wind_speed']} m/s")

def search_weather():
    city = city_entry.get()
    get_weather(city)

app = tk.Tk()
app.title("Weather App")

city_label = tk.Label(app, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

search_button = tk.Button(app, text="Search", command=search_weather)
search_button.pack()

weather_label = tk.Label(app, text="")
weather_label.pack()

temperature_label = tk.Label(app, text="")
temperature_label.pack()

description_label = tk.Label(app, text="")
description_label.pack()

wind_speed_label = tk.Label(app, text="")
wind_speed_label.pack()

app.mainloop()
