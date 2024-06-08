import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        report = {
            "City": data['name'],
            "Temperature": main['temp'],
            "Humidity": main['humidity'],
            "Pressure": main['pressure'],
            "Weather": weather['description'],
            "Wind Speed": wind['speed']
        }
        
        return report
    else:
        return None

def print_weather_report(report):
    if report:
        print(f"City: {report['City']}")
        print(f"Temperature: {report['Temperature']}°C")
        print(f"Humidity: {report['Humidity']}%")
        print(f"Pressure: {report['Pressure']} hPa")
        print(f"Weather: {report['Weather']}")
        print(f"Wind Speed: {report['Wind Speed']} m/s")
    else:
        print("City Not Found or Error in fetching data.")

if __name__ == "__main__":
    api_key = "2f5d89346aa959cf27bfcd37cfbb6d26"  # Replace with your OpenWeatherMap API key
    city_name = input("Enter city name: ")
    
    weather_report = get_weather(city_name, api_key)
    print_weather_report(weather_report)
